import polars as pl
from helpers.argparse import get_args
from sklearn.model_selection import train_test_split
from helpers.eda import get_column_value_frequency
import duckdb

args = get_args()
data_directory = "project/data/energy"
filename = "energy.parquet"
df = pl.read_parquet(f"{data_directory}/s_{filename}")

if args.verbose:
    print("\nSILVER DATA STRUCTURE ---")
    df.glimpse()

unique_ids = df.select("ID").unique()
print(f"Number of unique IDs: {len(unique_ids)}")

print("\nDATA PROCESSING ---")
# Do some mutations for modeling, remove junk data, and prepare for splitting
df = duckdb.sql(
    """
    SELECT
        ID
        , BuildingName
        , EUI_WN AS EuiWN
        , Year
        , Years
        , NumYears
        , Year - YearBuilt AS BuildingAge
        , PropertyGFABuildings AS TotalBuildingFloorSpace
        , CASE WHEN NumberofFloors > 1 THEN 1 ELSE 0 END AS HasMultipleFloors
        , CASE WHEN NumberofBuildings > 1 THEN 1 ELSE 0 END AS HasMultipleBuildings
        , CASE
            WHEN BuildingType LIKE 'Multifamily%' THEN 'MultiFamily'
            ELSE BuildingType
        END AS BuildingType
    FROM df
    -- Below filters remove some suspected junk rows
    WHERE NumberofFloors > 0
    AND NumberofBuildings > 0
    AND PropertyGFABuildings < 10000000 -- Remove a single problematic outlier
    """
).pl().with_row_index()

if args.verbose:
    df.glimpse()

if args.write:
    path = f"{data_directory}/g_{filename}"
    print(f"\nWRITING DATASETS TO {path} ---")
    df.write_parquet(path)
