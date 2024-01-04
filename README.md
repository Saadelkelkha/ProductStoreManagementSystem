# ProductStoreManagementSystem
This program implements a product store management system using classes for generic products, stores, books, and CDs. Products have attributes like name, prices, and quantity. Stores manage product stocks and transactions, and CDs/Books inherit from Products with specific attributes.

# More Details :
This program defines a set of classes related to managing products, stores, books, and CDs. Here's a breakdown of each class:

<b>Products</b>:

Represents a generic product with attributes such as name, purchase price, selling price, quantity, and description.
Provides methods to get and set various attributes.
Includes methods to display product details and check equality based on the product name.

<b>Stores</b>:

Represents a store with attributes like address and a stock of products.
Includes methods to add products to the stock, buy/sell products, and display the store's balance sheet.
Provides methods to get and set store attributes and check equality based on the store address.

<b>CDs</b> (inherits from Products):

Represents a specific type of product, a CD, with additional attributes such as author, interpreter, and title.
Inherits from the Products class and extends it with CD-specific attributes.
Includes methods to get and set CD attributes and check equality based on the author and interpreter.

<b>Books</b> (inherits from Products):

Represents another specific type of product, a book, with additional attributes such as author and publisher.
Inherits from the Products class and extends it with book-specific attributes.
Includes methods to get and set book attributes and check equality based on the author and publisher.

<b>Main</b>:

The program concludes with an example of using these classes to create instances of products, stores, books, and CDs. It demonstrates operations such as adding products to a store, buying and selling products, and displaying details and equality checks for various instances
