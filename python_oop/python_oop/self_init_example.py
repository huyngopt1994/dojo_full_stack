class User(object):
    name = "Anna"

anna = User()
print("anana's name", anna.name)
User.name = "Bob"
print ("ana's name after change:", anna.name)
bob = User()
print("bob's name:", bob.name)

class Chain(object):
    def print_name(self):
        print('my name is huy')
        return self
    def print_age(self):
        print("I'm 18 years old")
        return self

chain = Chain()
chain.print_name().print_age()