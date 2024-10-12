import requests
from bs4 import BeautifulSoup
import pandas as pd




# URL of the page you want to scrape
url = 'https://www.betterworldbooks.com/search/results'

# Send a GET request to the website
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract book details
    books = []

    for book in soup.select('.book-item'):  # Change selector based on the HTML structure
        title = book.select_one('.title').get_text(strip=True)
        author = book.select_one('.author').get_text(strip=True)
        price = book.select_one('.price').get_text(strip=True)
        isbn = book.select_one('.isbn').get_text(strip=True) if book.select_one('.isbn') else 'N/A'

        books.append({
            'title': title,
            'author': author,
            'price': price,
            'isbn': isbn
        })

    # Save to a CSV file
    df = pd.DataFrame(books)
    df.to_csv('books.csv', index=False)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
