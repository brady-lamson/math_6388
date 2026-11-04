import torch
import torch.nn as nn
import polars as pl
from helpers.argparse import get_args
from helpers.modeling import BinaryMLP, evaluate_binary_classifier
import os
import numpy as np
from scipy.optimize import minimize_scalar

args = get_args()

print("INGESTING AND PREPARING DATA ---")
path = "project/data/mushroom"
column = "spore_print_color"
dtype = pl.Float32
df = pl.read_parquet(f"{path}/g_mushroom.parquet")
splits = np.load(f"{path}/splits.npz")

# Transform datasets for modeling ---
X = df.drop("poisonous")
y = df.select("poisonous")

X_train = X[splits["train"]].to_dummies(columns=column, drop_first=True).to_torch(return_type="tensor", dtype=dtype)
X_test = X[splits["test"]].to_dummies(columns=column, drop_first=True).to_torch(return_type="tensor", dtype=dtype)
X_cal = X[splits["cal"]].to_dummies(columns=column, drop_first=True).to_torch(return_type="tensor", dtype=dtype)
y_train = y[splits["train"]].to_torch(return_type="tensor", dtype=dtype)
y_test = y[splits["test"]].to_torch(return_type="tensor", dtype=dtype)
y_cal = y[splits["cal"]].to_torch(return_type="tensor", dtype=dtype)

if args.verbose:
    print("\nTrain sets ---")
    print(X_train.shape, X_train.dtype)
    print(y_train.shape, y_train.dtype)
    print(y_train.unique())

    print("\nTest sets ---")
    print(X_test.shape, X_test.dtype)
    print(y_test.shape, y_test.dtype)
    print(y_test.unique())

    print("\nCalibration sets ---")
    print(X_cal.shape, X_cal.dtype)
    print(y_cal.shape, y_cal.dtype)
    print(y_cal.unique())

print("\nPREPARING THE MODEL ---")
torch.manual_seed(200)
MODEL_PATH = "project/models/mushroom/mushroom_nn.pt"
in_features=X_train.shape[1]
model = BinaryMLP(input_dim=in_features)
loss_fn = nn.BCEWithLogitsLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

if args.verbose:
    print("MODEL: ", model)
    print("LOSS FUNCTION: ", loss_fn)
    print("OPTIMIZER: ", optimizer)

model_exists = os.path.exists(MODEL_PATH)
if model_exists and not args.write:
    print(f"Model found at <{MODEL_PATH}>, loading model...")
    model.load_state_dict(torch.load(MODEL_PATH, weights_only=True))
else:
    if not model_exists:
        print(f'Model not found at <{MODEL_PATH}>, training model...')
    elif args.write:
        print("Model overwrite selected, training model...")
    n_epochs = 1500
    model.train()

    for epoch in range(n_epochs):
        logits = model(X_train)
        loss = loss_fn(logits, y_train.squeeze())

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if (epoch + 1) % 100 == 0:
            print(f"Epoch {epoch + 1:3d} | Loss: {loss.item():.4f}")

    torch.save(model.state_dict(), MODEL_PATH)

print("\nBEGINNING TEMPERATURE OPTIMIZATION ---")
model.eval()
with torch.no_grad():
    cal_logits = model(X_cal)
    test_logits = model(X_test)

def calibration_nll(log_temperature):
    # Convert log(T) to a positive temperature.
    temperature = np.exp(log_temperature)

    # Evaluate cross-entropy on calibration data only.
    # Cross-entropy accepts logits directly, without softmax.
    with torch.no_grad():
        loss = loss_fn(cal_logits / temperature, y_cal.squeeze())

    return loss.item()

# Optimize one scalar: log(T).
result = minimize_scalar(
    calibration_nll,
    bounds=(-15.0, 15.0),
    method="bounded",
)

if not result.success:
    raise RuntimeError(f"Temperature optimization failed: {result.message}")

temperature = float(np.exp(result.x))
print(f"Learned temperature: {temperature:.3f}")

# Convert test logits into probabilities before and after calibration.
# Use softmax because each image belongs to exactly one of ten classes.
print("EVALUATING MODEL BEFORE/AFTER CALIBRATION ---")
with torch.no_grad():
    probs_before = torch.sigmoid(test_logits)
    probs_after = torch.sigmoid(test_logits / temperature)

    print("\nBefore Calibration...")
    before_results = evaluate_binary_classifier(probs_before, y_test)
    print("\nAfter Calibration...")
    after_results = evaluate_binary_classifier(probs_after, y_test)