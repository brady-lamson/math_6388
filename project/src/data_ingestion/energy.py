import polars as pl

data_directory = "../../data/energy"
df = pl.read_csv(f"{data_directory}/b_seattle_energy_benchmark.csv", infer_schema_length=10000)

print("\nPROCESSING DATA - ORIGINAL DATA ---")
dimensions = df.shape
print(f"Rows: {dimensions[0]}\nColumns: {dimensions[1]}")
print(df.head())

print("\nINITIAL COLUMNS ---")
print(df.columns)

print("\nCOLUMNS NARROWED DOWN---")
columns = [
    "OSEBuildingID",
    "DataYear",
    "BuildingName",
    "BuildingType",
    "Neighborhood",
    "YearBuilt",
    "NumberofFloors",
    "NumberofBuildings",
    "PropertyGFABuildings",
    "EPAPropertyType",
    "SiteEUI(kBtu/sf)",
    "SiteEUIWN(kBtu/sf)"
]
df = (
    df
    .filter(
        (pl.col("Demolished") == "false") &
        (pl.col("SiteEUI(kBtu/sf)").is_not_null())
    )
    .select(columns)
    .rename({
        "SiteEUI(kBtu/sf)": "EUI",
        "SiteEUIWN(kBtu/sf)": "EUI_WN"
    })
)
with pl.Config(tbl_cols=-1):
    print(df.head(20))

print("\nPROCESSED DATA ---")
dimensions_new = df.shape
print(f"Rows: {dimensions_new[0]}\nColumns: {dimensions_new[1]}")
print(f"{round(dimensions_new[0]/dimensions[0] * 100, 5)}% of original {dimensions[0]} rows maintained.")
print(f"{round(dimensions_new[1]/dimensions[1] * 100, 5)}% of original {dimensions[1]} columns maintained.")


write = True
if write:
    print("\nWRITE SILVER TABLES ---")
    df.write_parquet(f"{data_directory}/s_energy.parquet")
else:
    print("Write is False, skipping write step")