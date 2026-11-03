import torch
import torch.nn as nn
from torchmetrics.classification import BinaryCalibrationError
import polars as pl
from helpers.argparse import get_args
from sklearn.metrics import precision_score, recall_score, f1_score, log_loss, confusion_matrix
import os

args = get_args()

print("INGESTING AND PREPARING DATA ---")
path = "project/data/mushroom"
column = "spore_print_color"
dtype = pl.Float32
X_train = pl.read_parquet(f"{path}/g_mushroom_xtrain.parquet").to_dummies(columns=column, drop_first=True).to_torch(return_type="tensor", dtype=dtype)
X_test = pl.read_parquet(f"{path}/g_mushroom_xtest.parquet").to_dummies(columns=column, drop_first=True).to_torch(return_type="tensor", dtype=dtype)
y_train = pl.read_parquet(f"{path}/g_mushroom_ytrain.parquet").to_torch(return_type="tensor", dtype=dtype)
y_test = pl.read_parquet(f"{path}/g_mushroom_ytest.parquet").to_torch(return_type="tensor", dtype=dtype)

if args.verbose:
    print("\nTrain sets ---")
    print(X_train)
    print(y_train)
    print(X_train.shape, X_train.dtype)
    print(y_train.shape, y_train.dtype)
    print(y_train.unique())

    print("\nTest sets ---")
    print(X_test)
    print(y_test)
    print(X_test.shape, X_test.dtype)
    print(y_test.shape, y_test.dtype)
    print(y_test.unique())

print("\nPREPARING THE MODEL ---")
torch.manual_seed(200)
MODEL_PATH = "project/models/mushroom/mushroom_log_reg.pt"
model = nn.Linear(
    in_features=X_train.shape[1],
    out_features=y_train.shape[1],
)
loss_fn = nn.BCEWithLogitsLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
if args.verbose:
    print("MODEL: ", model)
    print("LOSS FUNCTION: ", loss_fn)
    print("OPTIMIZER: ", optimizer)

if os.path.exists(MODEL_PATH):
    print(f"Model found at <{MODEL_PATH}>, loading model...")
    model.load_state_dict(torch.load(MODEL_PATH, weights_only=True))
else:
    print(f'Model not found at <{MODEL_PATH}>, training model...')
    n_epochs = 1500
    model.train()

    for epoch in range(n_epochs):
        logits = model(X_train)
        loss = loss_fn(logits, y_train)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if (epoch + 1) % 100 == 0:
            print(f"Epoch {epoch + 1:3d} | Loss: {loss.item():.4f}")

    torch.save(model.state_dict(), MODEL_PATH)

print("\nEVALUATING THE MODEL ---")
model.eval()

with torch.no_grad():
    test_logits = model(X_test)
    test_probabilities = torch.sigmoid(test_logits)
    test_predictions = (test_probabilities >= 0.5).float()

    accuracy = (test_predictions == y_test).float().mean()
    precision = precision_score(y_test, test_predictions)
    recall = recall_score(y_test, test_predictions)
    f1 = f1_score(y_test, test_predictions)
    nll = log_loss(y_test, test_predictions)
    conf_mat = confusion_matrix(y_test, test_predictions)
    ece = BinaryCalibrationError(n_bins=15)
    ece_value = ece(test_probabilities, y_test)

    print(f"\nACCURACY: {accuracy.item():.2%}")
    print(f"PRECISION: {precision:.2%}")
    print(f"RECALL: {recall:.2%}")
    print(f"F1-SCORE: {f1:.2%}")
    print(f"CONFUSION MATRIX:\n{conf_mat}")
    print(f"NLL: {round(nll, 5)}")
    print(f"BCE: {ece_value.item():.5f}")

