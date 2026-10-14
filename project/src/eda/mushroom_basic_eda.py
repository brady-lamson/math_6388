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

frequency_breakdown=True

if frequency_breakdown:
    print("\nFREQUENCY BREAKDOWN ---")
    for column in df.columns:
        print(f"\n{column} frequency ---")
        print(
            df
            .group_by(column)
            .agg(
                pl.len().alias("freq"),
                (pl.len() / dimensions[0]).alias("proportion")
            )
            .sort(by=column, descending=True)
        )