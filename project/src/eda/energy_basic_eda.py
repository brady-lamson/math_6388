import polars as pl
from src.helpers.eda import get_column_value_frequency

data_directory = "../../data/energy"
df = pl.read_parquet(f"{data_directory}/s_energy.parquet")

buildings = (
    df
    .select("OSEBuildingID")
    .unique()
    .shape[0]
)
print(f"\nNumber of Buildings in Dataset: {buildings}\n")

print(get_column_value_frequency(df, column_name="EPAPropertyType"))
print(get_column_value_frequency(df, column_name="BuildingType"))
with pl.Config(tbl_rows=-1):
    print(get_column_value_frequency(df, column_name="Neighborhood"))
    print(get_column_value_frequency(df, column_name="DataYear"))
