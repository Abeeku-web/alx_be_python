class Book:
    """ A class which models a book with attribute for the title, author and publication year."""
    def __init__(self, title, author, year): # initializes a Book instance with title, author and year.
        self.title = title
        self.author = author
        self.year = year

    def __del__(self): 
        print(f"Deleting {self.title}") # prints "Deleting (title of the book)" upon object deletion.

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.year}')"
    