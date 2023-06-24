import requests
from bs4 import BeautifulSoup
import json

url = "https://www.cricbuzz.com/profiles/26"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')

# Find the Batting Career Summary table by its class name
table = soup.find('table', class_='table cb-col-100 cb-plyr-thead')

# Initialize an empty list to store table data
data = []

# Extract table headers
headers = [header.text for header in table.find_all('th')]

# Extract table rows
rows = table.find_all('tr')

# Iterate over each row and extract the cell values
for row in rows:
    row_data = [cell.text for cell in row.find_all('td')]
    if row_data:  # Skip header row
        data.append(row_data)

# Create a dictionary to store the table data
table_data = {
    'headers': headers,
    'values': data
}

# Convert the dictionary to JSON
json_data = json.dumps(table_data, indent=4)

# Print or save the JSON data as per your requirement
print(json_data)