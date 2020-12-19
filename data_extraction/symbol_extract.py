import pandas as pd


def extract_symbol(file_path):
    df = pd.read_csv(file_path)
    symbol_list = list(df["Symbol"])
    return symbol_list

