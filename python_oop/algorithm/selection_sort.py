# step for selection search
# for example a0,a1,a2,a3, ... an => we sorted the lowest number firstly and swap it to the first posistion
# take this process for the next lowest , we have do 1 +2 + 3... + n  = n(n-1)/2 =>It will be the best case for O(n^2) algorithm

def selection_search(input):
    for i1 in range(0, len(input) -1):
        for i2 in range(i1, len(input)):
            if input[i1] > input[i2]:
                #swap it
                temp = input[i1]
                input[i1] = input[i2]
                input[i2] = temp


    return input
print(selection_search([1,52,5,66,11,33,99,12131,11,22,44,22,767,44,22,-1]))