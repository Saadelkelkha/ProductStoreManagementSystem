from produits import Products

class Books(Products):
    def __init__(self, name, purchase_price, selling_price, author, publisher):
        # Initialize book attributes using the parent class constructor
        super().__init__(name, purchase_price, selling_price) 
        self.__author = author 
        self.__publisher = publisher

    @property
    def get_author(self):
        return self.__author
    
    @property
    def get_publisher(self):
        return self.__publisher
    
    def set_author(self, author):
        # Set the author of the book
        self.__author = author

    def set_publisher(self, publisher):
        # Set the publisher of the book
        self.__publisher = publisher

    def __str__(self):
        # Return a formatted string representing the book
        return super().__str__() + f", Author: {self.get_author}, Publisher: {self.get_publisher}"

    def __eq__(self, other):
        # Check if two books are equal based on their author and publisher
        return (self.get_author == other.get_author) and (self.get_publisher == other.get_publisher)
