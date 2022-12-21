import pandas as pd
df_json = pd.read_json('data.json')
df_json.to_excel('input.xlsx')