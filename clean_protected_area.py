import pandas as pd

# Adjust skiprows if necessary (usually 3)
df = pd.read_csv("API_ER.LND.PTLD.ZS_DS2_en_excel_v2_23333.csv", skiprows=3)

df.columns = df.columns.str.strip()

id_vars = ['Country Name', 'Country Code']
year_columns = [col for col in df.columns if col not in id_vars]

df[year_columns] = df[year_columns].apply(pd.to_numeric, errors='coerce')

df_long = df.melt(id_vars=id_vars, value_vars=year_columns, var_name='Year', value_name='Value')

df_long['Year'] = df_long['Year'].astype(str).str.extract(r'(\d{4})')
df_long['Year'] = pd.to_numeric(df_long['Year'], errors='coerce')

df_long = df_long.dropna(subset=['Value']).reset_index(drop=True)

df_long.to_csv("protected_areas_long.csv", index=False)

print(df_long.head(10))
