import pandas as pd

def extract_data(path):
    # Header is on row index 2
    df = pd.read_excel(path, header=2)
    return df
