class Car(object):
    def __init__(self,price, speed, fuel, mileage):
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage

    def display_all(self):
        print ("Price : %s \nSpeed :%s \nFuel : %s\nMileage: %s\nTax: %s" % (self.price, self.speed,
                                                                             self.fuel, self.mileage, self.tax))



car1 = Car( 2000,'45mph','Full','25mgp')
car2 = Car( 3000, '55mph', 'Empty', '15mpg')

car1.display_all()
car2.display_all()
