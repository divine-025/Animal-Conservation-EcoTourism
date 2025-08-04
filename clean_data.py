import pandas as pd

# Step 1: Load data (skip metadata rows)
df = pd.read_csv("API_ER.LND.PTLD.ZS_DS2_en_excel_v2_23333.csv", skiprows=3)

# Step 2: Extract Rwanda row
rwanda_row = df[df['Country Name'].str.strip().str.lower() == 'rwanda']

# Step 3: Prepare for reshaping
id_vars = ['Country Name', 'Country Code']
year_columns = [col for col in rwanda_row.columns if col not in id_vars]

# Convert year columns to numeric
rwanda_row[year_columns] = rwanda_row[year_columns].apply(pd.to_numeric, errors='coerce')

# Step 4: Reshape wide to long format
rwanda_long = rwanda_row.melt(id_vars=id_vars,
                              value_vars=year_columns,
                              var_name='Year',
                              value_name='Value')

# Extract year as numeric
rwanda_long['Year'] = rwanda_long['Year'].astype(str).str.extract('(\d{4})')
rwanda_long['Year'] = pd.to_numeric(rwanda_long['Year'], errors='coerce')

# Drop rows with missing values
rwanda_long = rwanda_long.dropna(subset=['Value']).reset_index(drop=True)

# Step 5: Output
print(rwanda_long.head(10))

# Step 6: Save to CSV
rwanda_long.to_csv("rwanda_land_protection_long.csv", index=False)

