import polars as pl
import json

data_directory = "../../data/mushroom"
filename = "b_agaricus-lepiota"
df = pl.read_csv(f"{data_directory}/{filename}.data")

with open(f"{data_directory}/value_map.json", "r") as f:
    mapping = json.load(f)

# INITIAL DATA PROCESSING ---
## COLUMNS
df.columns = list(mapping.keys())

## VALUES
# Uses the json map to re-assign single character values to the actual words they represent
df = (
    df.with_columns(
        pl.col(column).replace(mapping[column]).alias(column)
        for column in mapping
    )
)

# # Write new dataframe
df.write_csv(file=f"{data_directory}/s_mushroom_processed.csv")