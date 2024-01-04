# Importing classes from modules
from cds import CDs
from livres import Books    
from magasinsss import Stores
from produits import Products

# Creating instances of Products class
hp = Products("Elitebook i5", 455, 466)
hp1 = Products("Elitebook i7", 1455, 1556)
hp2 = Products("Elitebook i11", 11455, 11466)

# Displaying details of the first product
print("Product Details:", hp)

# Checking if two products are equal
print("Equals Products:", hp == hp1, "\n")

# Creating instances of Stores class
mag = Stores("Socoma", [hp, hp1])
mag1 = Stores("Massira 2", [hp2])

# Adding a new product to the store
mag.add_product(hp2)
print(mag)

# Buying 20 units of the second product
mag.buy_product(1, 20)
print(mag)

# Selling 10 units of the second product
mag.sell_product(1, 10)
print(mag)

# Displaying the balance sheet of the store
print(mag.balance_sheet())

# Checking if two stores are equal
print("Equals Stores:", mag == mag1, "\n")

# Creating instances of Books class
liver = Books("To Kill a Mockingbird", 10, 15.99, "Harper Lee", "J.B.Lippincott & Co")
liver1 = Books("The Great Gatsby", 12.50, 19.99, "F. Scott Fitzgerald", "Charles Scribner's Sons")

# Displaying details of the first book
print("Book Details:", liver)

# Checking if two books are equal
print("Equals Books:", liver == liver1, "\n")

# Creating instances of CDs class
cd = CDs("Abbey Road", 14.99, 24.99, "The Beatles", "The Beatles", ["Come Together", "Something", "Oh! Darling"])
cd1 = CDs("Thriller", 12, 19.99, "Michael Jackson", "Michael Jackson", ["Thriller", "Billie Jean", "Beat It"])

# Displaying details of the first CD
print("CD Details:\n", cd)

# Checking if two CDs are equal
print("Equals CDs:", cd == cd1, "\n")
