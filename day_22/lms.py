class Library:
    def __init__(self, books, num_of_books):
        self._books = books
        self._num_of_books = num_of_books
        self._librarian_name = "Trishan Wagle"
        self._librarian_salary = "$99999"

    def print_all_books(self):
        print(f"Books in this library are:{', '.join(self._books)}")

    def add_book(self, new_book):
        self._books.append(new_book)
        self._num_of_books += 1

    @property
    def __librarian_details(self):
        return f"Name = {self._librarian_name}\nSalary = {self._librarian_salary}\nIt is sensitive information and must be kept private."
    
    @__librarian_details.setter
    def __librarian_details(self, new_librarian):
        self._librarian_name = new_librarian[0]
        self._librarian_salary = new_librarian[1]

    def get_num_of_books(self):
        print(self._num_of_books)


science_library = Library(["Physics", "Chemistry", "Biology"], 3)
science_library.add_book("A Brief History of Time")
science_library.print_all_books()
science_library.get_num_of_books()


computer_library = Library(["Java", "Python", "C++"], 3)
computer_library.add_book("JavaScript")
computer_library.print_all_books()
computer_library.get_num_of_books()


admin_library = Library(["HR", "Communication"], 2)
admin_library.add_book("Creative Thinking")
admin_library.print_all_books()
admin_library.get_num_of_books()

print(admin_library._Library__librarian_details) # due to Name Mangling we can access private methods/attributes like this
admin_library._Library__librarian_details = ("Wagle", "$123123")
print(admin_library._Library__librarian_details)