import requests
from bs4 import BeautifulSoup
import csv

# URL of the target site
url = 'https://economictimes.indiatimes.com/markets/stocks/news'
headers = {'User-Agent': 'Mozilla/5.0'}

# Request the page content
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all news blocks
stories = soup.find_all('div', class_='eachStory')

# Prepare CSV file
with open('scrape1.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Headline', 'URL', 'Summary'])  # CSV header

    for story in stories:
        h3 = story.find('h3')
        a_tag = story.find('a', href=True)
        p = story.find('p')

        headline = h3.get_text(strip=True) if h3 else ''
        link = "https://economictimes.indiatimes.com" + a_tag['href'] if a_tag else ''
        summary = p.get_text(strip=True) if p else ''

        writer.writerow([headline, link, summary])

print("✅ market_news.csv created successfully.")
