# Define a Product class with name, category, and price.

# Store at least 6 products.

# Use filter() + lambda to find all products costing > ₹1000.

# Print results in this format:

# makefile Copy Edit

class Product:
     def __init__(self,name,category,price):
         self.name = name
         self.category = category
         self.price = price
         
     def __str__(self):
         return f"Product_Name: {self.name} \nCategory: {self.category} \nPrice: {self.price} \n----------------------- "
     
p1 = Product("Phone", "Electronics", 15000)
p2 = Product("Tablet", "Electronics", 8000)
p3 = Product("Shoes", "Fashion", 900)
p4 = Product("Washing Machine", "Appliances", 22000)
p5 = Product("Pen", "Stationery", 50)
p6 = Product("Headphones", "Electronics", 1200)

product = [p1,p2,p3,p4,p5,p6]

costly_product = list(filter(lambda x:x.price > 1000,product))

for product in costly_product:
    print(product)