class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality


class Book:
    def __init__(self, title, author, uniqueId, genre):
        self.title = title
        self.author = author
        self.uniqueId = uniqueId
        self.genre = genre
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"{self.title} by {self.author.name} has been checked out.")
        else:
            print(f"{self.title} is already checked out.")

    def return_book(self):
        if self.checked_out:
            self.checked_out = False
            print(f"{self.title} by {self.author.name} has been returned.")
        else:
            print(f"{self.title} is not checked out.")

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author.name}\nuniqueId: {self.uniqueId}\nGenre: {self.genre}\nChecked Out: {self.checked_out}"


class Patron:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.checked_out_books = []

    def check_out_book(self, book):
        if len(self.checked_out_books) >= 3:
            print("You have reached the maximum number of books allowed to check out.")
            return
        if not book.checked_out:
            self.checked_out_books.append(book)
            book.check_out()
        else:
            print(f"{book.title} is already checked out.")

    def return_book(self, book):
        if book in self.checked_out_books:
            self.checked_out_books.remove(book)
            book.return_book()
        else:
            print(f"You have not checked out {book.title}.")

    def __str__(self):
        checked_out_books_str = ", ".join(
            [book.title for book in self.checked_out_books])
        return f"Name: {self.name}\nID: {self.id}\nChecked Out Books: {checked_out_books_str if checked_out_books_str else 'None'}"


if __name__ == "__main__":
    author1 = Author("Chetan Bhagat", "Indian")
    author2 = Author("Stephen King", "American")

    book1 = Book("Revolution 2020",
                 author1, "876787612", "Motivation")
    book2 = Book("The Shining", author2, "9780385121675", "Novel")

    patron1 = Patron("Rahul Yadav", 101)
    patron2 = Patron("Dhruv Kumar", 102)

    patron1.check_out_book(book1)
    patron1.check_out_book(book2)
    patron2.check_out_book(book1)
    patron1.return_book(book1)
    patron2.return_book(book1)

    print("\nBook details:")
    print(book1)
    print(book2)
    print("\nPatron details:")
    print(patron1)
    print(patron2)
