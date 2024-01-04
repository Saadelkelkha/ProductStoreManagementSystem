from produits import Products

class CDs(Products):
    def __init__(self, name, purchase_price, selling_price, author, interpreter, title):
        # Initialize CD attributes using the parent class constructor
        super().__init__(name, purchase_price, selling_price)
        self.__author = author
        self.__interpreter = interpreter
        self.__title = title
        
    @property
    def get_author(self):
        return self.__author
    
    @property
    def get_interpreter(self):
        return self.__interpreter
    
    @property
    def get_title(self):
        return self.__title
    
    def set_author(self, author):
        # Set the author of the CD
        self.__author = author

    def set_interpreter(self, interpreter):
        # Set the interpreter of the CD
        self.__interpreter = interpreter

    def set_title(self, title):
        # Set the title of the CD
        self.__title = title

    def __str__(self):
        # Return a formatted string representing the CD
        return super().__str__() + f", Author: {self.get_author}, Interpreter: {self.get_interpreter}, Title: {self.get_title}"

    def __eq__(self, other):
        # Check if two CDs are equal based on their author and interpreter
        return (self.get_author == other.get_author) and (self.get_interpreter == other.get_interpreter)
