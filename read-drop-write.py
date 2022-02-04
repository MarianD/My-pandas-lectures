import pandas as pd

df = pd.read_csv("1000 Sales Records.csv")
print(df.sample(5))

df_without_totals = df.drop(columns=[name for name in df.columns if name.startswith("Total") ], inplace=True)
print(df_without_totals.sample(5))

df_without_totals.to_csv("1000 objednavok.csv", index=False)
