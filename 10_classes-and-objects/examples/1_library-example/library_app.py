from library_tools.book import Book


if __name__ == '__main__':
    
    print("Welcome to our Library App")
    print("--------------------------")

    book = Book("The Lord of the Rings", "J.R.R. Tolkien", 1000)

    # let's print the books properties.
    print("The properties of our book are:")
    print(f"Title: {book.title}")
    print(f"Author: {book.author}")

    # let's print the book.
    print("The book is:")
    print(book)              # this calls Book.__str__()

