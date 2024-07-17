class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self): #for a fancy output
        return f"{self.title} by {self.author}, published in {self.year}."
    
    def __repr__(self): #for developer to avoid ambiguous values
        return f"Book({self.title!r}, {self.author!r}, {self.year!r})"
    
    def __del__(self):
        print(f"Deleting {self.title}")

#book1 = Book("Deuces", "Ouko", 31)
#print(book1)
#print(repr(book1))
#del book1