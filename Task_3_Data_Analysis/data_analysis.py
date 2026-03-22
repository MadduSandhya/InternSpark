import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load CSV
df = pd.read_csv("sales_data.csv")

print("\n--- Original Data ---")
print(df)

# Step 2: Data Cleaning
print("\nMissing Values:")
print(df.isnull().sum())

df = df.drop_duplicates()

# Add Total column
df["Total"] = df["Price"] * df["Quantity"]

print("\n--- Cleaned Data ---")
print(df)

# Step 3: Filtering
electronics = df[df["Category"] == "Electronics"]

print("\n--- Electronics Products ---")
print(electronics)

# Step 4: Grouping
category_sales = df.groupby("Category")["Total"].sum()
city_sales = df.groupby("City")["Total"].sum()

print("\n--- Sales by Category ---")
print(category_sales)

print("\n--- Sales by City ---")
print(city_sales)

# Step 5: Summary Statistics
print("\n--- Summary Statistics ---")
print(df.describe())

# Step 6: Insights
print("\n--- Insights ---")
print("Top Category:", category_sales.idxmax())
print("Top City:", city_sales.idxmax())

# Step 7: Graphs (Optional but good)
category_sales.plot(kind="bar", title="Sales by Category")
plt.show()

city_sales.plot(kind="bar", title="Sales by City")
plt.show()