from library_tools.book import Book
from library_tools.library import Library


if __name__ == '__main__':
    
    print("Welcome to our Library App")
    print("--------------------------")

    # step 6: create a library
    library = Library("Edmonton Public Library")
    print(library)  # -> "Edmonton Public Library"

    book = Book("The Lord of the Rings", "J.R.R. Tolkien", 1000)



