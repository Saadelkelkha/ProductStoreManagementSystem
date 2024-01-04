class Products:
    def __init__(self, name, purchase_price, selling_price):
        # Initialize product attributes
        self.__name = name
        self.__purchase_price = purchase_price
        self.__selling_price = selling_price
        self.__quantity = 0
        self.__description = "No description"
    
    @property
    def get_name(self):
        return self.__name
    
    @property
    def get_purchase_price(self):
        return self.__purchase_price
    
    @property
    def get_selling_price(self):
        return self.__selling_price
    
    @property
    def get_quantity(self):
        return self.__quantity
    
    @property
    def get_description(self):
        return self.__description
    
    def set_name(self, name):
        # Set product name
        self.__name = name

    def set_purchase_price(self, purchase_price):
        # Set product purchase price
        self.__purchase_price = purchase_price

    def set_selling_price(self, selling_price):
        # Set product selling price
        self.__selling_price = selling_price

    def set_quantity(self, quantity):
        # Set quantity of the product
        self.__quantity = quantity

    def set_description(self, description):
        # Set product description
        self.__description = description

    def __str__(self):
        # Return a formatted string representing the product
        return f"Name: {self.get_name}, Description: {self.get_description}, Quantity: {self.get_quantity}, Purchase Price: {self.get_purchase_price}, Selling Price: {self.get_selling_price}"
    
    def __eq__(self, other):
        # Check if two products are equal based on their names
        return self.get_name == other.get_name
