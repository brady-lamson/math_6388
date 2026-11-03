import polars as pl

def compare_split_column_values(train, test, column_name):
    print("RUNNING compare_split_column_values")
    train_set = set(train[column_name])
    test_set = set(test[column_name])
    result = train_set == test_set
    if not result:
        print(f"FAILED - train_set <{train_set}> != test_set <{test_set}>")
    else:
        print("PASSED")

    return result