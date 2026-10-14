import polars as pl

data_directory = "../../data/rainfall"
df = pl.read_csv(f"{data_directory}/b_usa_rain_prediction_dataset_2024_2025.csv")

print("\nPROCESSING DATA - ORIGINAL DATA ---")
dimensions = df.shape
print(f"Rows: {dimensions[0]}\nColumns: {dimensions[1]}")
print(df.head())

print("\nINITIAL COLUMNS ---")
print(df.columns)

df = (
    df
    .rename(lambda col: col.lower().replace(' ', '_'))
    .drop("rain_tomorrow")
)

print("\nUPDATED COLUMNS ---")
print(df.columns)

print("\nPROCESSING DATES ---")
df = (
    df
    .with_columns(pl.col("date").str.to_date().alias("date"))
    .with_columns(pl.col("date").dt.ordinal_day().alias("day_of_year"))
    .filter(pl.col("precipitation") > 0)
)

print("\nWRITING DATA ---")
df.write_parquet(f"{data_directory}/s_rainfall.parquet")