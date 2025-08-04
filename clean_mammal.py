import pandas as pd

# Load file and correctly get headers from row 4 (index 3)
df = pd.read_csv("API_EN.MAM.THRD.NO_DS2_en_excel_v2_21073.csv", skiprows=3)

# Rename columns explicitly based on inspection
df.columns = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'] + [str(y) for y in range(1960, 2025)]

# Keep only the useful columns
df = df[['Country Name', 'Country Code'] + [str(y) for y in range(2000, 2025)]]

# Reshape to long format
df_long = df.melt(id_vars=['Country Name', 'Country Code'],
                  var_name='Year',
                  value_name='Value')

# Drop rows with missing values
df_long = df_long.dropna(subset=['Value']).reset_index(drop=True)

# Save cleaned data
df_long.to_csv("mammal_species_threatened_long.csv", index=False)

print("✅ Cleaned mammal species data saved as 'mammal_species_threatened_long.csv'")
print(df_long.head(10))
