from product import Product
from product_manager import ProductManager

manager = ProductManager()

p1 = Product("Laptop", 1000, 5)
p2 = Product("Telefon", 500, 10)
p3 = Product("Monitor", 300, 7)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

print("Lista proizvoda:")
manager.show_products()

print("Ukupna vrednost inventara:")
print(manager.total_value())