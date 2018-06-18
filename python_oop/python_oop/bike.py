class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print("Price :%s , max speed is %s, total miles is %s" %
              (self.price, self.max_speed, self.miles))

    def ride(self):
        print ("Riding")
        self.miles += 10
        return self
    def reverse(self):
        if self.miles ==0:
            print("Can't reverse it's the end")
            return self
        print ("Reversing")
        self.miles -=5
        return self

bike1 = Bike(200, "25mph")
bike2 = Bike(150, "15mph")
bike3 = Bike(250, "35mph")

bike1.reverse()
bike2.reverse()
bike3.reverse()

bike1.displayInfo()
bike2.displayInfo()
bike3.displayInfo()

bike2.ride()
bike2.ride()

for i in range(4):
    bike2.reverse()
bike2.displayInfo()
#ride and reverse
