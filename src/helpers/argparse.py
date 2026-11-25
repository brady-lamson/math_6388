import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Sets basic result writing options")
    parser.add_argument("-w", "--write", action="store_true", help="Write parquet file")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging")
    parser.add_argument("-c", "--cutoff", type=float, help="Cutoff for binary classification")
    args = parser.parse_args()

    return args