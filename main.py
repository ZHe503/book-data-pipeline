import requests
import csv


book = input("Whats the title of the book")

r = requests.get(f"https://openlibrary.org/search.json?q={book}")

if r.status_code != 200:
    print("This book doesnt exist")

else:
    data = r.json()

    books = data["docs"]

    if not books:
        print("No books found for:")
    else:
        books_data = []

        for i in range(5):
            book = books[i]

            title = book.get("title", "Unknown")

            authors = book.get("author_name")
            if authors:
                author = authors[0]
            else:
                author = "Unknown"

            year = book.get("first_publish_year", "Unknown")

            book_data = {
                "title": title,
                "author": author,
                "year": year
            }

            books_data.append(book_data)

        print(books_data)


with open("books.csv", "w", newline="") as file:
    fieldnames = ["title", "author", "year"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(books_data)