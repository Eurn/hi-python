import pandas as pd
df = pd.read_json(r'example.json')
df.to_csv(r'example.csv', index=None)
