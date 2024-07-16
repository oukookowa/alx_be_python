class NotInStockError(Exception):
    """Custom exception for handling out-of-stock movies."""

    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Sorry, the Movie '{self.title}' is out of stock."
    
x = NotInStockError("Boom")
print(x)