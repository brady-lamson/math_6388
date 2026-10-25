# Source: https://catalog.data.gov/dataset/building-energy-benchmarking-data-2015-present

import polars as pl
import argparse

parser = argparse.ArgumentParser(description="Sets basic result writing options")
parser.add_argument("-w", "--write", action="store_true", help="Write parquet file")
parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging")
args = parser.parse_args()

data_directory = "project/data/energy"
df = pl.read_csv(f"{data_directory}/b_seattle_energy_benchmark.csv", infer_schema_length=10000)

print("\nPROCESSING DATA - ORIGINAL DATA ---")
dimensions = df.shape
print(f"Rows: {dimensions[0]}\nColumns: {dimensions[1]}")
if args.verbose:
    print(df.head())

print("\nINITIAL COLUMNS ---")
print(df.columns)

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
        "SiteEUIWN(kBtu/sf)": "EUI_WN",
        "OSEBuildingID": "ID",
        "DataYear": "Year"
    })
    .with_columns(
        # Process numeric columns read in as strings due to commas
        (pl.col("PropertyGFABuildings").str.replace_all(pattern=",", value="").cast(pl.Int64).alias("PropertyGFABuildings")),
        (pl.col("EUI").str.replace_all(pattern=",", value="").cast(pl.Float32).alias("EUI")),
        (pl.col("EUI_WN").str.replace_all(pattern=",", value="").cast(pl.Float32).alias("EUI_WN")),
        # Some year columns for purely diagnostic purposes
        (pl.col("Year") == 2025).alias("Year2025"),
        pl.concat_list(
            pl.col("Year").sort().implode().over("ID")
        ).alias("Years"),
    )
    .with_columns((pl.col("Years").list.len()).alias("NumYears"))
)
num_columns_added = 3 # hard coded, for reporting later

print("\nCOLUMNS NARROWED DOWN ---")
print(df.columns)

grain = ["ID", "Year"]
print(f"\nChecking for duplicates at expected grain: <{grain}>")
dupes = (
    df
    .group_by(grain)
    .len()
    .sort("len", descending=True)
    .filter(pl.col("len") > 1)
)

if dupes.shape[0] > 0:
    print("[FAIL] Duplicates found ---")
    print(dupes)
else:
    print("[PASSED] No duplicates found")

print("\nPROCESSED DATA ---")
dimensions_new = df.shape
print(f"Rows: {dimensions_new[0]}\nColumns: {dimensions_new[1]}\nNew Columns: {num_columns_added}")
print(f"{round(dimensions_new[0]/dimensions[0] * 100, 5)}% of original {dimensions[0]} rows maintained.")
print(f"{round((dimensions_new[1] - num_columns_added)/dimensions[1] * 100, 5)}% of original {dimensions[1]} columns maintained.")

if args.verbose:
    print(df.head(5))

print("\nDATA WRITE STEP ---")
write = True
if args.write:
    print("\nWriting silver tables")
    path = f"{data_directory}/s_energy.parquet"
    df.write_parquet(path)
    print(f"TABLE WRITTEN TO {path}")
else:
    print("Write is False, skipping write step")