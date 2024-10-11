# Define the years and product types
years = [2022, 2023, 2024]
product_types = ["book", "game"]

# Load sales data
sales_data = {}
for year in years:
    for product in product_types:
        sales_data[f"{product}_sales_{year}"] = load(f"data/{product}_sales_{year}.csv")

# Calculate total sales for each year
total_sales = {}
for year in years:
    total_sales[year] = sum_sales(sales_data[f"book_sales_{year}"], sales_data[f"game_sales_{year}"])
