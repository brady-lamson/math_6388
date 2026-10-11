import polars as pl

data_directory = "../../data/mushroom"
filename = "mushroom_processed"
df = pl.read_csv(f"{data_directory}/{filename}.csv")

print("\nDATA STRUCTURE ---")
dimensions = df.shape
print(f"Rows: {dimensions[0]}\nColumns: {dimensions[1]}")

print("\nMISSING DATA - Columns with nonzero null counts ---")
print(
    df.null_count().select(
        [column for column in df.columns if df[column].null_count() > 0]
    )
)

print("\nRESPONSE FREQUENCY ---")
print(
    df
    .group_by("poisonous")
    .agg(
        pl.len().alias("freq"),
        (pl.len() / dimensions[0]).alias("proportion")
    )
    .sort(by="proportion", descending=True)
)