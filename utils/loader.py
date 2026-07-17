import pandas as pd


def load_data(file):

    if file.name.endswith(".csv"):
        return pd.read_csv(file)

    return pd.read_excel(file)