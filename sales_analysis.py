# 📌 Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# 📌 Step 2: Load CSV
df = pd.read_csv("sales_data.csv")

# 📌 Step 3: Explore Data
print("First 5 rows:\n", df.head())
print("\nData Info:\n", df.info())
print("\nSummary:\n", df.describe())

# 📌 Step 4: Total Sales
total_sales = df['Sales'].sum()
print("\nTotal Sales:", total_sales)

# 📌 Step 5: Sales by Category
category_sales = df.groupby('Category')['Sales'].sum()
print("\nSales by Category:\n", category_sales)

# Plot
category_sales.plot(kind='bar', title="Sales by Category", color='skyblue')
plt.ylabel("Total Sales")
plt.show()

# 📌 Step 6: Sales by Region
region_sales = df.groupby('Region')['Sales'].sum()
print("\nSales by Region:\n", region_sales)

# Plot
region_sales.plot(kind='pie', autopct='%1.1f%%', title="Sales by Region")
plt.ylabel("")  
plt.show()

# 📌 Step 7: Trend Over Time
df['Date'] = pd.to_datetime(df['Date'])
daily_sales = df.groupby('Date')['Sales'].sum()

# Plot
daily_sales.plot(kind='line', marker='o', title="Daily Sales Trend")
plt.ylabel("Sales")
plt.show()
