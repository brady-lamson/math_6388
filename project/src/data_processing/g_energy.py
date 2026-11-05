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

# Do some mutations for modeling, remove junk data, and prepare for splitting
df = duckdb.sql(
    """
    SELECT
        ID
        , BuildingName
        , EUI_WN AS EuiWN
        , Year
        , Years
        , Year - YearBuilt AS BuildingAge
        , PropertyGFABuildings AS TotalBuildingFloorSpace
        , CASE WHEN NumberofFloors > 1 THEN 1 ELSE 0 END AS HasMultipleFloors
        , CASE WHEN NumberofBuildings > 1 THEN 1 ELSE 0 END AS HasMultipleBuildings
        , CASE
            WHEN BuildingType LIKE 'Multifamily%' THEN 'MultiFamily'
            ELSE BuildingType
        END AS BuildingType
        -- Below case handles rows with a single year, we want to force those into specific splits
        -- Same with any buildings with no 2025 info, those should only be in train.
        , CASE
            WHEN NumYears == 1 AND Year < 2025 THEN 'train'
            WHEN NumYears == 1 AND Year == 2025 THEN 'holdout'
            WHEN 2025 NOT IN Years THEN 'train_candidate'
            ELSE NULL
        END AS Split
    FROM df
    -- Below filters remove some suspected junk rows
    WHERE NumberofFloors > 0
    AND NumberofBuildings > 0
    AND PropertyGFABuildings < 10000000 -- Remove a single problematic outlier
    """
).pl()

if args.verbose:
    print("\nPROCESSED DATA FOR MODELING ---")
    unique_ids = df.select("ID").unique()
    print(f"Number of unique IDs: {len(unique_ids)}")
    df.glimpse()
    print("ROWS WITH FORCED SPLITS ---")
    duckdb.sql(
        """
        SELECT
            ID
            , BuildingName
            , Year
            , Split
        FROM df
        WHERE Split IS NOT NULL
        """
    ).pl().glimpse()

print("\nPREPARING SPLITS ---")
print("Deciding on holdout ids")
holdout_candidate_ids = duckdb.sql(
    """
    SELECT ID, BuildingType
    FROM df
    WHERE Year = 2025
    AND Split IS NULL
    """
).pl()

# Leaves 80% For train/test
rest, holdout = train_test_split(holdout_candidate_ids, test_size=0.2, random_state=100, stratify=holdout_candidate_ids.select("BuildingType"))
rest = rest.select("ID")
holdout = holdout.select("ID") # TODO: Combine this with "Split" == 'Holdout' before saving

rest_df = duckdb.sql(
    """
    SELECT *
    FROM df
    WHERE Split NOT IN ('train', 'holdout')
    """
)

df.glimpse()