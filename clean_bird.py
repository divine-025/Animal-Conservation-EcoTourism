import pandas as pd

# Load with correct header
df = pd.read_csv("API_EN.BIR.THRD.NO_DS2_en_excel_v2_21056.csv", skiprows=3)

# Rename columns
df.columns = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'] + [str(y) for y in range(1960, 2025)]

# Keep relevant years only
df = df[['Country Name', 'Country Code'] + [str(y) for y in range(2000, 2025)]]

# Reshape into long format
df_long = df.melt(id_vars=['Country Name', 'Country Code'],
                  var_name='Year',
                  value_name='Value')

# Drop missing values
df_long = df_long.dropna(subset=['Value']).reset_index(drop=True)

# Save cleaned file
df_long.to_csv("bird_species_threatened_long.csv", index=False)

print("✅ Cleaned bird species data saved as 'bird_species_threatened_long.csv'")
print(df_long.head(10))

