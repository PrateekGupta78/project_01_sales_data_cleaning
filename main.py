import pandas as pd

# 1. Load CSV
df = pd.read_csv("sales.csv")

# 2. Clean column names
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

# 3. Remove empty rows
df = df.dropna(how="all")

# 4. Remove duplicates
df = df.drop_duplicates()

# 5. Handle missing values
df = df.dropna()

# 6. Save clean file
df.to_csv("clean_sales.csv", index=False)


