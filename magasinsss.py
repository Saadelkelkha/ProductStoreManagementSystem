from produits import Products  

class Stores:
    def __init__(self, address, product_stock):
        # Initialize store attributes
        self.__address = address
        self.__product_stock = product_stock

    @property
    def get_address(self):
        return self.__address
    
    def set_address(self, new_address):
        # Set store address
        self.__address = new_address

    @property
    def get_product_stock(self):
        return self.__product_stock
    
    def set_product_stock(self, stock):
        # Set store product stock
        self.__product_stock = stock

    def add_product(self, p1):
        # Add a product to the store stock
        self.__product_stock.append(p1)

    def buy_product(self, product_reference, quantity):
        # Increase the quantity of a product in the store stock
        self.__product_stock[product_reference].set_quantity(
            quantity + self.__product_stock[product_reference].get_quantity)

    def sell_product(self, product_reference, quantity):
        # Sell a quantity of a product from the store stock
        if self.__product_stock[product_reference].get_quantity >= quantity:
            self.__product_stock[product_reference].set_quantity(
                self.__product_stock[product_reference].get_quantity - quantity)
        else:
            print("Not enough stock to sell")

    def __eq__(self, other):
        # Check if two stores are equal based on their addresses
        return self.get_address == other.get_address
    
    def __str__(self):
        # Return a formatted string representing the store and its product stock
        s = ""
        for element in self.__product_stock:
            s += str(element) + "\n"
        return f"Store Address: {self.get_address}\nProduct Stock: \n{s}\n"

    def balance_sheet(self):
        # Calculate the total value of the store's product stock
        total_value = 0

        for product in self.__product_stock:
            total_value += (product.get_purchase_price * product.get_quantity)

        return f"Total Value of Stock: {total_value} DH"
                                                     