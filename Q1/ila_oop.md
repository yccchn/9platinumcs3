# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
I can use encapsulation by creating a Product class that contains the product name, price, and stock quantity. I can keep these properties inside the class and use methods such as get_stock() and update_stock() to access or modify them. This can help me keep the product information organized and prevent other parts of the program from changing the data directly.

### 2. Abstraction
I can apply abstraction by creating simple methods for common inventory actions while hiding the complicated details behind them. For example, I can create a sell_product() method that reduces stock quantity without requiring me to see all the calculations behind the method. This can make my program easier to understand and use.

### 3. Inheritance
I can use inherirance by creating a general Product class and then creating classes such as SchoolProduct and FoodProduct that inherit from it. I can reuse properties such as name, price, and stock from the Product class instead of writing them again. This can help me reduce repeated code and make my inventory system easier to expand.

### 4. Polymorphism
I can apply polymorphism by giving different product classes the same method but allowing each class to perform it differently. For example, I can give both FoodProduct and SchoolProduct a display_info() method, but each class can display information specific to its product type. This allows me to use one method name while handling different types of products.

## Reflection
Among the four pillars of Object-Oriented Programming, I believe abstraction would be the most useful for improving the sari-sari store inventory system. I can use abstraction to hide complicated processes ad only show the actions that I need such as sell_product() or add_stock(). This can make the program easier for me to understand and use because I do not have to worry about the details of how each method works. In short, I think abstraction is the most useful as it can make the inventory system simpler and more organized.