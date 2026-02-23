

class Library:

    def __init__(self):
        self.book1 = "Python"
        self.book2 = "C"
        self.book3 = "Java"
        self.book4 = "DSA"

    def show_books(self):
        print("Available Books:")
        print(self.book1)
        print(self.book2)
        print(self.book3)
        print(self.book4)

    def issue_book(self):

        print(" -Python issued- ")
        self.book1 = "Issued"

    def return_book(self):

        print(" -Python returned- ")
        self.book1 = "Python"


# Main Program

obj = Library()

obj.show_books()
print()
obj.issue_book()
print()
obj.show_books()
print()
obj.return_book()
print()
obj.show_books()
