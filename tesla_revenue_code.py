import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, "html.parser")

tables = soup.find_all("table")
for table in tables:
    if "Tesla Quarterly Revenue" in str(table):
        revenue_table = table
        break

tesla_revenue = pd.read_html(str(revenue_table))[0]
tesla_revenue.columns = ['Date', 'Revenue']
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
tesla_revenue['Revenue'] = tesla_revenue['Revenue'].str.replace("\\$", "").str.replace(",", "")

# Display the last five rows
print(tesla_revenue.tail())
