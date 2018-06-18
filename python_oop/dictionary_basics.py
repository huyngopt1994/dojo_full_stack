personal_dict = {
    "name" : "Anna",
    "age": 101,
    "country": "The United States",
    "language": "python"
}

def display_info(my_dict):
    print("My name is %s" % my_dict['name'])
    print("My age is %s" % my_dict['age'])
    print("My contry of birth is %s" % my_dict['country'])
    print("My favorite language is %s" % my_dict['language'])

display_info(personal_dict)