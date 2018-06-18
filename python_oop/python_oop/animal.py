class Animal(object):
    def __init__(self,name,health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -=1
    def run(self):
        self.health -=5
    def display(self):
        print(self.health)


class Dog(Animal):
    def __init__(self, name):
        self.name = name
        self.health = 160
    def pet(self):
        self.health +=5

class Dragon(Animal):
    def __init__(self, name):
        self.name = name
        self.health = 170
    def fly(self):
        self.health -=10
    def display_health(self):
        self.display()
        print("I'm a dragon")

dragon1 = Dragon('huy')
dragon1.display_health()
