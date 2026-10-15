import polars as pl

def get_column_value_frequency(df: pl.DataFrame, column_name: str):

    if column_name not in df.columns:
        raise ValueError(f"Column <{column_name}> not found in provided DataFrame.")

    print(f"Collecting <{column_name}> Values ---")
    return(
        df
        .select(
            pl.col(column_name).value_counts()
        )
        .unnest()
        .sort(column_name)
    )