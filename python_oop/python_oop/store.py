from product import  Product
class Store(object):
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        for index, product in enumerate(self.products):
            if product.item_name == product_name:
                del self.products[index]


    def inventory(self):
        for product in self.products:
            product.display_info()

product1 = Product(200, 'a', 150)
product2 = Product(300,'b', 250)
product3 = Product(400,'a',200)

my_store = Store([product1,product2,product3], 'vietnam', 'huy')

my_store.inventory()
my_store.add_product(Product(500,'c',540))
print('-----------')
my_store.inventory()
print('------------')
my_store.remove_product('a')
my_store.inventory()