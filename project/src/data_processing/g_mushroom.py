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
        (pl.col("odor") != "none").alias("has_odor"),
        (pl.col("gill_color") == "buff").alias("gill_color_buff"),
        (
            pl.when(pl.col("spore_print_color").is_in(["brown", "black", "white", "chocolate"]))
            .then(pl.col("spore_print_color"))
            .otherwise(pl.lit("other"))
        ).alias("spore_print_color")
    )
    .drop(
        [
            "stalk_root",       # missing data
            "veil_type",        # column is all one value
            "gill_attachment",  # Used for gill attached
            "gill_spacing",     # Used for gill spacing crowded
            "gill_size",        # Used for gill size narrow
            "stalk_shape",      # Used for stalk shape tapered
            "gill_color",       # used for gill color buff
            "veil_color",       # No meaningful relationship with response
            "ring_number",      # Maybe revisit, but just doesn't appear meaningful enough
            "gill_attached",    # Way too sparse for attached gills, basically 50/50 for bulk of rows
            "habitat",          # Too many categories, none that really jump out
            "population",       # Potentially usable, but need to narrow down.
            "cap_color",        # Too many categories, uninformative on its own
            "odor",             # Used for has_odor
            "ring_type",        # Potentially usable, need to narrow down,
            "cap_surface",      # Meh
            "cap_shape",        # Meh,
            # Dropping the below for additional cleanup
            "stalk_surface_above_ring",
            "stalk_surface_below_ring",
            "stalk_color_above_ring",
            "stalk_color_below_ring",
        ]
    )
)

print("\nCONVERTING BOOLEANS TO INTEGERS ---")
df = (
    df
    .with_columns(
        pl.selectors.by_dtype(pl.Boolean).cast(pl.Int64)
    )
)

if args.verbose:
    print("\nGOLD DATA STRUCTURE ---")
    df.glimpse()

print("\nDATA WRITE STEP ---")
if args.write:
    print("WRITE IS TRUE - Writing gold table")
    path = f"{data_directory}/g_{filename}"
    df.write_parquet(path)
    print(f"TABLE WRITTEN TO {path}")
else:
    print("Write is False, skipping write step")