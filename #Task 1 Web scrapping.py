#Task 1 Web scrapping


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://books.toscrape.com/catalogue/page-1.html"

titles = []
prices = []
ratings = []

for page in range(1, 6):
    response = requests.get(f"http://books.toscrape.com/catalogue/page-{page}.html")
    soup = BeautifulSoup(response.content, 'html.parser')
    books = soup.find_all('article', class_='product_pod')

    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        rating = book.p.get('class')[1]  

        titles.append(title)
        prices.append(price)
        ratings.append(rating)

df = pd.DataFrame({
    'Title': titles,
    'Price': prices,
    'Rating': ratings
})

df.to_csv('books_data.csv', index=False)

print("✅ Web scraping complete! Data saved to books_data.csv")
