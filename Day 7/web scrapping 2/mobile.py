# Importing required libraries
from bs4 import BeautifulSoup
import pandas as pd
import os

# Load the HTML file
html_file = 'web-scrapp_mobile.html'

if not os.path.exists(html_file):
    print(f"Error: File '{html_file}' not found.")
    exit()

with open(html_file, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all phone cards
cards = soup.find_all('div', style=lambda x: x and 'width: 300px' in x)

# List to store all phone data
mobile_data = []

# Loop through each card and extract info
for card in cards:
    try:
        name = card.find('strong').text.strip()
        condition = card.find('span', style=lambda x: x and 'background-color' in x).text.strip()
        color_tag = card.find('p')
        color = color_tag.text.replace('Color:', '').strip() if color_tag else 'N/A'

        original_price_tag = card.find('span', string=lambda x: x and 'Original' in x)
        original_price = original_price_tag.text.replace('Original:', '').strip() if original_price_tag else 'N/A'

        savings_tag = card.find_all('span')[-1]
        savings = savings_tag.text.replace('Savings:', '').strip() if savings_tag else 'N/A'

        sold_price_tag = card.find('p', style=lambda x: x and 'color: green' in x)
        sold_price = sold_price_tag.text.replace('Sold:', '').strip() if sold_price_tag else 'N/A'

        # Append to list
        mobile_data.append({
            'Name': name,
            'Condition': condition,
            'Color': color,
            'Original Price': original_price,
            'Savings': savings,
            'Sold Price': sold_price
        })
    except Exception as e:
        print(f"Error extracting a card: {e}")

# Convert to DataFrame
df = pd.DataFrame(mobile_data)

# Show the DataFrame
print(df)

# Save to CSV
df.to_csv('mobile_auction_data.csv', index=False)
print("\nData has been saved to 'mobile_auction_data.csv'")
