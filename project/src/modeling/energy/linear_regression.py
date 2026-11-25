# NOTE: USE NB2 IN LECTURE NOTEBOOKS FOR REFERENCE

import torch
import torch.nn as nn
import polars as pl
from helpers.argparse import get_args
from helpers.modeling import BinaryMLP, evaluate_binary_classifier
import os
import numpy as np
import json

args = get_args()

print("INGESTING AND PREPARING DATA ---")
path = "project/data/energy"
response = "EuiWN"
dtype = pl.Float32
df = pl.read_parquet(f"{path}/g_energy.parquet")
splits = np.load(f"{path}/splits.npz")

# Transform datasets for modeling ---
X = (
    df
    .drop([response, "ID", "index", "BuildingName", "Years", "NumYears"])
    .with_columns((pl.col("Year") - 2015).alias("Year")) # Change year to a year index
)
y = (
    df
    .select(response)
    .with_columns(pl.col(response).log().alias(response))
)

if args.verbose:
    df.glimpse()
    y.glimpse()

cat_column = "BuildingType"
# Two sets of train, 1 test, 1 holdout ---
X_train_full = X[splits["train_full"]]
X_train_dedupe = X[splits["train_deduplicated"]]
X_test = X[splits["test"]]
X_holdout = X[splits["holdout"]]

print("\nSTANDARDIZING NUMERIC COLUMNS AND HANDLING TORCH CONVERSION ---")
numeric_columns = ["BuildingAge", "TotalBuildingFloorSpace"]

means = X_train_full.select(numeric_columns).mean()
stds = X_train_full.select(numeric_columns).std()
if args.verbose:
    print("MEANS: ", means)
    print("STDS: ", stds)

def standardize_df(df, means, stds, numeric_columns):
    return df.with_columns(
        [
            ((pl.col(c) - means[c][0]) / stds[c][0]).alias(c)
            for c in numeric_columns
        ]
    )

X_train_full = (
    standardize_df(X_train_full, means, stds, numeric_columns)
    .to_dummies(columns=cat_column, drop_first=True)
    .to_torch(return_type="tensor", dtype=dtype)
)
X_train_dedupe = (
    standardize_df(X_train_dedupe, means, stds, numeric_columns)
    .to_dummies(columns=cat_column, drop_first=True)
    .to_torch(return_type="tensor", dtype=dtype)
)
X_test = (
    standardize_df(X_test, means, stds, numeric_columns)
    .to_dummies(columns=cat_column, drop_first=True)
    .to_torch(return_type="tensor", dtype=dtype)
)
X_holdout = (
    standardize_df(X_holdout, means, stds, numeric_columns)
    .to_dummies(columns=cat_column, drop_first=True)
    .to_torch(return_type="tensor", dtype=dtype)
)

y_train_full = y[splits["train_full"]].to_torch(return_type="tensor", dtype=dtype)
mean = torch.mean(y_train_full)
std = torch.std(y_train_full)
if args.verbose:
    print("RESPONSE MEAN: ", mean)
    print("RESPONSE STD: ", std)
y_train_full = (y_train_full - mean) / std
y_train_dedupe = y[splits["train_deduplicated"]].to_torch(return_type="tensor", dtype=dtype)
y_train_dedupe = (y_train_dedupe - mean) / std
y_test = y[splits["test"]].to_torch(return_type="tensor", dtype=dtype)
y_test = (y_test - mean) / std
y_holdout = y[splits["holdout"]].to_torch(return_type="tensor", dtype=dtype)
y_holdout = (y_holdout - mean) / std

print("\nPREPARING THE MODEL ---")
torch.manual_seed(300)
SHARED_PATH = "project/models/energy"
MODEL_A_PATH = f"{SHARED_PATH}/linreg_full.pt"
model = nn.Linear(
    in_features=X_train_full.shape[1],
    out_features=1,
)
learning_rate = 0.02
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
if args.verbose:
    print("MODEL: ", model)
    print("LOSS FUNCTION: ", loss_fn)
    print("OPTIMIZER: ", optimizer)

baseline_pred = torch.full_like(
    y_train_full,
    y_train_full.mean()
)

baseline_loss = loss_fn(baseline_pred, y_train_full)

print("Baseline MSE:", baseline_loss.item())

model_exists = os.path.exists(MODEL_A_PATH)
if model_exists and not args.write:
    print(f"Model found at <{MODEL_A_PATH}>, loading model...")
    model.load_state_dict(torch.load(MODEL_A_PATH, weights_only=True))
else:
    if not model_exists:
        print(f'Model not found at <{MODEL_A_PATH}>, training model...')
    elif args.write:
        print("Model overwrite selected, training model...")
    n_epochs = 3000
    model.train()

    for epoch in range(n_epochs):
        y_pred = model(X_train_full)
        loss = loss_fn(y_pred, y_train_full)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if (epoch + 1) % 100 == 0:
            print(f"Epoch {epoch + 1:3d} | Loss: {loss.item():.4f}")

    torch.save(model.state_dict(), MODEL_A_PATH)