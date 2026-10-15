import polars as pl

data_directory = "../../data/healthcare"
rate_df = pl.read_csv(f"{data_directory}/Rate_PUF.csv")

print("\nPROCESSING DATA - ORIGINAL DATA ---")
dimensions = rate_df.shape
print(f"Rows: {dimensions[0]}\nColumns: {dimensions[1]}")
print(rate_df.head())

print("\nINITIAL COLUMNS ---")
print(rate_df.columns)

rate_df = (
    rate_df
    .filter(
        (pl.col("BusinessYear") == 2026) &
        (pl.col("Age") == "30") #&
        # (pl.col("Tobacco") == "No Preference")
    )
    .select(
        "PlanId",
        "StateCode",
        "RatingAreaId",
        "IssuerId",
        # "SourceName",
        "Tobacco",
        "IndividualRate"
    )
    .unique()
)

with pl.Config(tbl_cols=-1, tbl_rows=-1):
    print(rate_df.head(50))

print("\nPROCESSED DATA ---")
dimensions_new = rate_df.shape
print(f"Rows: {dimensions_new[0]}\nColumns: {dimensions_new[1]}")
print(f"{round(dimensions_new[0]/dimensions[0] * 100, 5)}% of original {dimensions[0]} rows maintained.")
print(f"{round(dimensions_new[1]/dimensions[1] * 100, 5)}% of original {dimensions[1]} columns maintained.")


write = False
if write:
    print("\nWRITE SILVER TABLES ---")
    rate_df.write_parquet(f"{data_directory}/s_rates.parquet")
else:
    print("Write is False, skipping write step")