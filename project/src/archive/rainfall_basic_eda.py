import polars as pl
import matplotlib.pyplot as plt
from math import log

data_directory = "../../data/rainfall"
filename = "s_rainfall"
df = pl.read_parquet(f"{data_directory}/{filename}.parquet")

print("\nDATA STRUCTURE ---")
dimensions = df.shape
print(f"Rows: {dimensions[0]}\nColumns: {dimensions[1]}")

print("\nMISSING DATA - Columns with nonzero null counts ---")
null_df = (
    df
    .null_count()
    .select(
        [column for column in df.columns if df[column].null_count() > 0]
    )
)

if null_df.shape == (0, 0):
    print("NULL CHECK PASSED: No columns have missing values.")
else:
    print(null_df)

print("\nNUMERIC DATA OVERVIEW ---")
with pl.Config(tbl_cols=-1):
    print(
        df
        .drop(["location", "date", "day_of_year"])
        .describe()
    )

print("\nALL LOCATIONS AND THEIR ROW COUNTS ---")
with pl.Config(tbl_rows=-1):
    print(df.select(pl.col("location").value_counts()).unnest("location"))

print("\nDATE OVERVIEW ---")

print("\nPLOTTING RESPONSE ---")
# Overview of the response, get more detailed distribution of precipitation
df = (
    df
    .with_columns(pl.col("precipitation").log().alias("log_precipitation"))
)
plt.hist(df["precipitation"], edgecolor="black")
plt.xlabel("Precipitation")
plt.ylabel("Frequency")
plt.title("Response Distribution - Non-zero Rainfall")
plt.savefig("../../images/rainfall/response_hist.png")
plt.close()

# Total rainfall per location maybe?
with pl.Config(tbl_rows=-1):
    print(
        df
        .group_by("location")
        .agg(
            pl.sum("precipitation").alias("total_rainfall"),
            pl.col("date").n_unique().alias("unique_dates")
        )
    )
# plt.barh(df["location"], df["precipitation"])
# plt.show()

# Basic line plot of rainfall per day of year?
