import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the news website
url = "https://www.bbc.com/news"  # You can replace this with any news URL

# Send a GET request to the website
response = requests.get(url)

# Parse the content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the headlines (This will depend on the website's HTML structure)
headlines = soup.find_all('h3')  # Modify this based on the actual structure of the website

# Extract headlines and links
links = [headline.find('a')['href'] for headline in headlines if headline.find('a')]

# Create a dictionary to hold the data
data = {'Headline': [headline.text.strip() for headline in headlines], 'Link': links}

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('latest_news.csv', index=False)
