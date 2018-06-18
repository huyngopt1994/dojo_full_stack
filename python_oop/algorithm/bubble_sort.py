#[a0,a1,a2,a3]
# for a list size n  we will do n step :
# for per element in this list , compare it and the next and swap it
# in the word case it's is n*n = O(n^2)
# in the best case it's  O(n) => So we will use it when try to implement easily and in the small  list

def  sort(input):
    for _ in range(0, len(input)):
        sorted = False
        for index in range(0, len(input)-1):
            if input[index] > input[index+1]:
                temp = input[index]
                input[index] = input[index+1]
                input[index+1] = temp
                sorted = True

        if sorted is False:
            break

    return (input)

print(sort([1,52,5,66,11,33,99,12131,11,22,44,22,767,44,22,-1]))
