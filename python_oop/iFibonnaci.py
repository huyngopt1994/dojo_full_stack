my_fibonnaci = [0,1,1]
def generate_fibonaci(number):
    if number ==0:
        return my_fibonnaci[:1]
    elif number ==1:
        return my_fibonnaci[:2]
    elif number ==2:
        return my_fibonnaci[:]

    for i in range(3, number+1):
        new_element = my_fibonnaci[i-1]+ my_fibonnaci[i-2]
        my_fibonnaci.append(new_element)

generate_fibonaci(6)
print (my_fibonnaci)