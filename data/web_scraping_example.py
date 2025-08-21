import requests
from bs4 import BeautifulSoup

# Define the URL of the website to scrape
url = 'https://example.com/blog'

# Send a GET request to fetch the HTML content of the page
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all article titles (assuming titles are in <h2> tags)
articles = soup.find_all('h2', class_='post-title')

# Extract and print the titles
for idx, article in enumerate(articles, 1):
    title = article.get_text(strip=True)
    print(f"Article {idx}: {title}")