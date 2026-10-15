import polars as pl

data_directory = "../../data/healthcare"
plan_df = pl.read_csv(f"{data_directory}/plan_attributes_PUF.csv", infer_schema_length=10000)

print("\nPROCESSING DATA - ORIGINAL DATA ---")
dimensions = plan_df.shape
print(f"Rows: {dimensions[0]}\nColumns: {dimensions[1]}")
print(plan_df.head())

print("\nINITIAL COLUMNS ---")
print(plan_df.columns)

columns_to_keep = [
    "StandardComponentId", "PlanId", "StateCode", "IssuerId",
    "MarketCoverage",  "PlanType", "MetalLevel",
    "CSRVariationType",
    "TEHBDedInnTier1Individual", "TEHBInnTier1IndividualMOOP"
]
dollar_columns = ["TEHBDedInnTier1Individual", "TEHBInnTier1IndividualMOOP"]
plan_small = (
    plan_df
    .filter(
        (pl.col("DentalOnlyPlan") != "Yes") &
        (pl.col("BusinessYear") == 2026)
    )
    .select(columns_to_keep)
    # Process value columns formatted like $6,100 and convert them to intger values
    .with_columns(
        pl.col(column)
        .str.replace_many(patterns=["$", ",", " "], replace_with=[""])
        .str.to_integer()
        .alias(column)
        for column in dollar_columns
    )
    # Extract out variant ids like 12345-01, 12345-02, etc as their own column
    # Turn StandardComponentId into the actual PlanId to match with Rates dataset
    .with_columns(
        (pl.col("PlanId").alias("PlanKey")),
        (pl.col("PlanId").str.extract(pattern=r"-(\d*$)").str.to_integer().alias("PlanVariantId")),
        (pl.col("StandardComponentId").alias("PlanId"))
    )
    .drop("StandardComponentId")
)

print("Variant ID Values ---")
print(
    plan_small
    .select(
        pl.col("PlanVariantId").value_counts()
    )
    .unnest()
    .sort("PlanVariantId")
)

print("CSR Variant Type Values ---")
with pl.Config(tbl_rows=-1):
    print(
        plan_small
        .select(
            pl.col("CSRVariationType").value_counts()
        )
        .unnest()
        .sort("CSRVariationType")
    )

print("Filter for smallest ID per plan")
plan_small = (
    plan_small
    .filter(
        (pl.col("PlanVariantId") == pl.col("PlanVariantId").min())
        .over("PlanId")
    )
)

# Verify one row per PlanId
print("\nCHECKING PlanId UNIQUENESS")
plan_id_freq = (
    plan_small
    .select(pl.col("PlanId").value_counts())
    .unnest()
    .filter(pl.col("count") > 1)
)

if plan_id_freq.shape[0] > 1:
    print(plan_id_freq)
else:
    print("PASSED - All PlanIds are unique")

print("\nPROCESSED DATA ---")
dimensions_new = plan_small.shape
print(f"Rows: {dimensions_new[0]}\nColumns: {dimensions_new[1]}")
print(f"{round(dimensions_new[0]/dimensions[0] * 100, 5)}% of original {dimensions[0]} rows maintained.")
print(f"{round(dimensions_new[1]/dimensions[1] * 100, 5)}% of original {dimensions[1]} columns maintained.")


write = False
if write:
    print("\nWRITE SILVER TABLES ---")
    plan_small.write_parquet(f"{data_directory}/s_plans.parquet")
else:
    print("\nWrite is False, skipping write step")