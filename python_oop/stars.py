def print_starts(my_list):
    for e in my_list:
        if type(e) is int:
            print ('*'*e)
        else :
            print (e[0].lower()*len(e))

print_starts( [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])