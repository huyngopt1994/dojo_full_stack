name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
name_short = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane"]
name_long = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar", "Huy"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1,list2):
    if len(list1) >= len(list2):
        new_dict  = dict(zip(list1, list2))
    else:
        new_dict = dict(zip(list2,list1))
    return new_dict

print(make_dict(name,favorite_animal))
print(make_dict(name_short,favorite_animal))
print(make_dict(name_long,favorite_animal))