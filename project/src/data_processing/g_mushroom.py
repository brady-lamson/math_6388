import polars as pl
from helpers.argparse import get_args

args = get_args()
data_directory = "project/data/mushroom"
filename = "mushroom.parquet"
df = pl.read_parquet(f"{data_directory}/s_{filename}")

if args.verbose:
    print("\nSILVER DATA STRUCTURE ---")
    df.glimpse()

df = (
    df
    .with_columns(
        # Boolean conversions ---
        (pl.col("poisonous") == "poisonous").alias("poisonous"),
        (pl.col("bruises") == "bruises").alias("bruises"),
        (pl.col("gill_attachment") == "attached").alias("gill_attached"),
        (pl.col("gill_spacing") == "crowded").alias("gill_spacing_crowded"),
        (pl.col("gill_size") == "narrow").alias("gill_size_narrow"),
        (pl.col("stalk_shape") == "tapering").alias("stalk_shape_tapered"),
        (pl.col("odor") != "none").alias("has_odor")
    )
    .drop(
        [
            "stalk_root",       # missing data
            "veil_type",        # column is all one value
            "gill_attachment",
            "gill_spacing",
            "gill_size",
            "stalk_shape",
            "veil_color",       # No meaningful relationship with response
            "ring_number",      # Maybe revisit, but just doesn't appear meaningful enough
            "gill_attached"     # Way too sparse for attached gills, basically 50/50 for bulk of rows
        ]
    )
)

if args.verbose:
    print("\nGOLD DATA STRUCTURE ---")
    df.glimpse()

print("\nDATA WRITE STEP ---")
if args.write:
    print("\nWriting gold table")
    path = f"{data_directory}/g_{filename}"
    df.write_parquet(path)
    print(f"TABLE WRITTEN TO {path}")
else:
    print("Write is False, skipping write step")