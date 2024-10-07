#create class Book
class Book:
    def __init__(self, title, author, available=True):
        self.title=title
        self.author=author
        self.available=available
    #use array to store library collection of book
class Library:
    def __init__(self):
        self.book=[]
    #Implement methods to add books, search for books by title or author, and update book availability using lambdas.
    def add_book(self, book):
        self.book.append(book)
    def search_by_title(self, title):
        search_title =  lambda book: book.title.lower() == title.lower()
        return list(filter(search_title,self.book))
    def search_by_author(self, author):
        search_author = lambda book: book.author.lower()==author.lower()
        return list(filter(search_author, self.book))
    def update_book_availability(self, title, available):
        update_book=lambda book: setattr(book, 'available', available) if book.title.lower()==title.lower() else None
        return list(map(update_book, self.book))
book1=Book("Python Programming", "John Smith")
book2=Book("Data Structures and Algorithms", "Jane Doe")
book3 = Book("Web Development with Python", "John Smith")
        #add books to library
library=Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
    # Search for books by title
print("Books with title 'Python Programming':")
for book in library.search_by_title("Python Programming"):
    print(f"- {book.title} by {book.author}")

# Search for books by author
print("\nBooks by author 'John Smith':")
for book in library.search_by_author("John Smith"):
    print(f"- {book.title} by {book.author}")

# Update book availability
library.update_book_availability("Data Structures and Algorithms", False)

# Check updated availability
print("\nAvailability of 'Data Structures and Algorithms':")
for book in library.search_by_title("Data Structures and Algorithms"):
    print(f"- {book.title} is {'available' if book.available else 'not available'}")

        


