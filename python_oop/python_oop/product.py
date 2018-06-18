class Product(object):
    def __init__(self, price, item_name, weight, status="for sale"):
        self.price =price
        self.item_name = item_name
        self.weight = weight
        self.status = "for sale"

    def sell(self):
        self.status = "Sold"
        return self

    def add_tax(self, tax):
        self.price += self.price*tax
        return self

    def return_something(self, reason):
        if reason == 'defective':
            self.status = 'defective'
            self.price = 0
        elif reason == 'new':
            self.status = 'for sale'
        else :
            self.status = 'used'
            self.price = 0.8*self.price
        return self

    def display_info(self):
        print("Item name %s and have price %s ,weight :%s and status is %s" % (self.item_name,
                                                                               self.price,
                                                                               self.weight,
                                                                               self.status))


