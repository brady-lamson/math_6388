import polars as pl
from helpers.tests import  compare_split_column_values
from sklearn.model_selection import train_test_split
from helpers.argparse import get_args

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
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=100,
    stratify=df["spore_print_color"]
)

if args.verbose:
    print("\nEnsuring spore print color was stratified correctly")
    print(compare_split_column_values(X_train, X_test, "spore_print_color"))

if args.write:
    print("\nWRITE IS TRUE, saving splits ---")
    path = "project/data/mushroom"
    print("Printing X Train")
    X_train.write_parquet(f"{path}/g_mushroom_xtrain.parquet")
    print("Printing X Test")
    X_test.write_parquet(f"{path}/g_mushroom_xtest.parquet")
    print("Printing y Train")
    y_train.to_frame().write_parquet(f"{path}/g_mushroom_ytrain.parquet")
    print("Printing y Test")
    y_test.to_frame().write_parquet(f"{path}/g_mushroom_ytest.parquet")
    print("SUCCESS - All splits saved")
else:
    print("\nWRITE IS FALSE, skipping save step ---")