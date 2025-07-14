import pandas as pd
import json

def load_json(path):
    with open(path, 'r') as f:
        data = json.load(f)
    return pd.json_normalize(data)

def basic_clean(df):
    df = df.dropna(subset=['wallet', 'action'])
    df['amount'] = df['amount'].fillna(0)
    return df
