import polars as pl
from helpers.eda import get_column_value_frequency

# General idea here:
# Look at 2025 buildings, any only in 2025 are guaranteed for test set
# For others, stratify sample on the rest.
# Then, look at buildings without 2025 rows. Pull random row for those IDs for train set.

data_directory = "project/data/energy"
df = pl.read_parquet(f"{data_directory}/s_energy.parquet")

df_2025 = df.filter(pl.col("Year") == 2025)
only_2025 = df_2025.filter(pl.col("NumYears") == 1)
print(f"Number of buildings only in 2025: {only_2025.shape[0]}")

all_id_years = df.select("ID")