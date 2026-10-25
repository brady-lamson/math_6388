import polars as pl
import json
from helpers.argparse import get_args

args = get_args()
data_directory = "project/data/mushroom"
filename = "b_agaricus-lepiota"
df = pl.read_csv(f"{data_directory}/{filename}.data")

with open(f"{data_directory}/value_map.json", "r") as f:
    mapping = json.load(f)

print("\nPROCESSING DATA - ORIGINAL DATA ---")
dimensions = df.shape
print(f"Rows: {dimensions[0]}\nColumns: {dimensions[1]}")
if args.verbose:
    print(df.head())

print("\nINITIAL COLUMNS ---")
print(df.columns)

print("\nPROCESSED COLUMNS ---")
df.columns = list(mapping.keys())
print(df.columns)

# Uses the json map to re-assign single character values to the actual words they represent
print("\nMAPPING SINGLE LETTER CELL VALUES TO REAL VALUES ---")
df = (
    df.with_columns(
        pl.col(column).replace(mapping[column]).alias(column)
        for column in mapping
    )
)

print("\nPROCESSED DATA ---")
dimensions_new = df.shape
print(f"Rows: {dimensions_new[0]}\nColumns: {dimensions_new[1]}")
print(f"{round(dimensions_new[0]/dimensions[0] * 100, 5)}% of original {dimensions[0]} rows maintained.")
print(f"{round((dimensions_new[1])/dimensions[1] * 100, 5)}% of original {dimensions[1]} columns maintained.")

if args.verbose:
    print("\nPROCESSED DATA SNIPPET ---")
    print(df.head())

print("\nDATA WRITE STEP ---")
if args.write:
    print("\nWriting silver tables")
    path = f"{data_directory}/s_mushroom.parquet"
    df.write_parquet(path)
    print(f"TABLE WRITTEN TO {path}")
else:
    print("Write is False, skipping write step")