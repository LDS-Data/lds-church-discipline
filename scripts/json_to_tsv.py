if __name__=="__main__":
    import argparse
    import pandas as pd

    parser = argparse.ArgumentParser(description='Expand JSON by processing various fields.')
    parser.add_argument("filename", help="Path to JSON to expand")

    args = parser.parse_args()

    data = pd.read_json(args.filename, orient='records')
    data.to_csv(args.filename.replace(".json",".tsv"), sep="\t", index=False)
