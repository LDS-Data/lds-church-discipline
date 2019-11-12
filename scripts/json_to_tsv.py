if __name__=="__main__":
    import pandas as pd

    data = pd.read_json("discipline.json", lines=True)
    data.to_dsv("discipline.tsv", sep="\t")
