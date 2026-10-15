
# Parent class for all publications
class Publication:
    def __init__(self, title, author):
        # Initialize private attributes
        self.__title = title
        self.__author = author

    # Display publication information
    def display_info(self):
        print("Title:", self.__title)
        print("Author:", self.__author)

# Book class inherits from Publication
class Book(Publication):
    def __init__(self, title, author, number_pages):
        # Initialize the parent class attributes
        super().__init__(title, author)

        # Set the default number of pages
        self.__number_pages = 0
        self.set_number_of_pages(number_pages)

    # Validate and set the number of pages
    def set_number_of_pages(self, number_pages):
        if number_pages > 0:
            self.__number_pages = number_pages
        else:
            print("Number of pages must be positive")

    # Display book information
    def display_info(self):
        super().display_info()
        print("Number of pages:", self.__number_pages)

# Magazine class inherits from Publication
class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        # Initialize the parent class attributes
        super().__init__(title, author)

        # Set the default issue number
        self.__issue_number = 0
        self.set_issue_number(issue_number)

    # Validate and set the issue number
    def set_issue_number(self, issue_number):
        if issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("Issue number must be positive")

    # Display magazine information
    def display_info(self):
        super().display_info()
        print("Issue number:", self.__issue_number)


# Create a Publication object
pub1 = Publication(
    "Journal of Experimental Psychology",
    "Ratchiff, R. & Van Dongen, H."
)

# Create a Book object
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)

# Create a Magazine object
mag1 = Magazine("National Geographic", "Various Authors", 202)


# Display Publication information
print("Publication Information:")
pub1.display_info()

# Display Book information and test invalid input
print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()

# Display Magazine information
print("\nMagazine Information:")
mag1.display_info()
