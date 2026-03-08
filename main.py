from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()

p1 = Product("Laptop pro", 1200, 3)
p2 = Product("samsung", 600, 8)
p3 = Product("Monitor HD", 350, 5)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

cart = Cart()
cart.add_to_cart(p1)
cart.add_to_cart(p2)
cart.add_to_cart(p3)

cart.show_cart()
print("Total amount to pay:", cart.total_amount())