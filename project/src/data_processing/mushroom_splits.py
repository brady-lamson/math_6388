import polars as pl
from helpers.tests import  compare_split_column_values
from helpers.argparse import get_args
from helpers.modeling import three_way_indices
import numpy as np

args = get_args()

data_directory = "project/data/mushroom"
df = pl.read_parquet(f"{data_directory}/g_mushroom.parquet")

X = df.drop("poisonous")
y = df["poisonous"]

if args.verbose:
    print("Printing data snippet ---")
    print("\nPrinting X")
    print(X.glimpse())
    print("\nPrinting y")
    print(y)


print("\nCreating splits ---")
splits = three_way_indices(y, stratify_column=df["spore_print_color"])
print(splits)
if args.verbose:
    print("\nEnsuring spore print color was stratified correctly")
    print(compare_split_column_values(df[splits["train"]], df[splits["test"]], "spore_print_color"))
    print(compare_split_column_values(df[splits["test"]], df[splits["cal"]], "spore_print_color"))

if args.write:
    np.savez("project/data/mushroom/splits.npz", **splits)
else:
    print("\nWRITE IS FALSE, skipping save step ---")
