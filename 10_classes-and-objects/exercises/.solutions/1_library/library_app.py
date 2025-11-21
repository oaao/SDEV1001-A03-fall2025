from library_tools.book import Book
from library_tools.library import Library


if __name__ == '__main__':
    
    print("Welcome to our Library App")
    print("--------------------------")

    library = Library("Edmonton Public Library")
    print(library)  # -> "Edmonton Public Library"

    # first, list the books before we've added any
    library.list_books()  # -> "Library is empty!"

    book = Book("The Lord of the Rings", "J.R.R. Tolkien", 1000)
    bookTwo = Book("The Wheel of Time", "Robert Jordan", 690)
    bookThree = Book("The Way of Kings", "Brandon Sanderson", 1200)
    bookFour = Book("Mistborn", "Brandon Sanderson", 640)

    books_to_add = (book, bookTwo, bookThree, bookFour)  # just for easy looping
    for b in books_to_add:
        library.add_book(b)

    library.list_books()

    # exercise 1: try to check out an existing book & a nonexistent book
    library.checkout_book("Mistborn")        # will remove from library
    library.checkout_book("Giovanni's Room") # will print out that the title doesn't exist
