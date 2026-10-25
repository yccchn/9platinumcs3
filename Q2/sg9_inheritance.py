# creates the parent class Publication
class Publication:
    def __init__(self, title, author):
        self.__title = title # stores the title
        self.__author = author # stores the author

    # gets the title
    def get_title(self):
        return self.__title

    # gets the author
    def get_author(self):
        return self.__author

    # updates the title
    def set_title(self, title):
        self.__title = title

    # updates the author
    def set_author(self, author):
        self.__author = author

    # displays publication information
    def display_info(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")

# creates Book as a subclass of Publication
class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author) # initializes parent attributes
        self.__number_of_pages = number_of_pages # stores page count

    # gets the number of pages
    def get_number_of_pages(self):
        return self.__number_of_pages

    # updates the number of pages
    def set_number_of_pages(self, number_of_pages):
        if number_of_pages > 0: # checks if the page count is positive
            self.__number_of_pages = number_of_pages
        else:
            print("Warning! Pages must be positive.")


# creates Magazine as a subclass of Publication
class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author) # initializes parent attributes
        self.__issue_number = issue_number # stores the issue number

    # gets the issue number
    def get_issue_number(self):
        return self.__issue_number

    # updates the issue number
    def set_issue_number(self, issue_number):
        if issue_number > 0: # checks if the issue number is positive
            self.__issue_number = issue_number
        else:
            print("Issue number must be positive.")


# creates the objects
pub1 = Publication(
    "Journal of Experimental Psychology",
    "Ratcliff, R. & Van Dongen, H."
)
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)


# displays publication information
print("Publication Information")
pub1.display_info()

# displays book information
print("\nBook Information")
book1.set_number_of_pages(-670) # tests an invalid page count
book1.display_info()
print(f"Number of Pages: {book1.get_number_of_pages()}")

# displays magazine information
print("\nMagazine Information")
mag1.display_info()
print(f"Issue Number: {mag1.get_issue_number()}")
