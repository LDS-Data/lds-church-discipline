if __name__=="__main__":
    import pandas as pd

    data = pd.read_json("discipline.json", lines=True)
    data.to_csv("discipline.tsv", sep="\t", index=False)
