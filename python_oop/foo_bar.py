# reserved by using recursion
__all__ =['recurive']
def recurive(my_string):
    if len(my_string) <2:
        return my_string
    return recurive(my_string[1:]) + my_string[0]

print(recurive('xin chao'))