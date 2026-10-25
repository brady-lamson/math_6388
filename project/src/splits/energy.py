import polars as pl
from src.helpers.eda import get_column_value_frequency

data_directory = "../../data/energy"
df = pl.read_parquet(f"{data_directory}/s_energy.parquet")

# Test over to tell when a building shows up multiple times
print(
    df
    .with_columns(
        pl.concat_list(
            pl.col("DataYear").sort().implode().over("OSEBuildingID")
        )
        .alias("DataYears"),
    )
    .with_columns((pl.col("DataYears").list.len()).alias("NumYears"))
)

# print(
#     df
#     .group_by("OSEBuildingID")
#     .len()
#     .sort("len", descending=True)
# )
#
# grain_violations = (
#     df
#     .group_by("OSEBuildingID", "DataYear")
#     .len()
#     .filter(pl.col("len") > 1)
# )
#
# if grain_violations.shape[0] > 0:
#     print(grain_violations)