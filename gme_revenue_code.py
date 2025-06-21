import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, "html.parser")

tables = soup.find_all("table")
for table in tables:
    if "GameStop Quarterly Revenue" in str(table):
        revenue_table = table
        break

gme_revenue = pd.read_html(str(revenue_table))[0]
gme_revenue.columns = ['Date', 'Revenue']
gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]
gme_revenue['Revenue'] = gme_revenue['Revenue'].str.replace("\\$", "").str.replace(",", "")

# Display the last five rows
print(gme_revenue.tail())
