import requests
from bs4 import BeautifulSoup
import csv

# Define the URL to scrape
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

# Send a request to the website and get the HTML content
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")

# Find all product boxes
boxes = soup.find_all("div", class_="col-md-4 col-xl-4 col-lg-4")

# Initialize lists to store names and prices
names = []
prices = []

# Extract names
name_elements = soup.find_all("a", class_="title")
for name in name_elements:
    names.append(name.text.strip())

# Extract prices
price_elements = soup.find_all("h4", class_="price float-end card-title pull-right")
for price in price_elements:
    prices.append(price.text.strip())

# Ensure the length of names and prices are the same
if len(names) != len(prices):
    print("Warning: The number of names and prices do not match.")
    
# Combine names and prices into a list of tuples
data = list(zip(names, prices))

# Define the CSV file name
csv_filename = 'products.csv'

# Write data to CSV file
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['Name', 'Price'])
    # Write the data
    writer.writerows(data)

print(f"Data has been written to {csv_filename}")
