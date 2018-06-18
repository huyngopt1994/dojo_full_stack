input = [2,3,5,7,6]
temp = input[0]
input[0] = input[-1]
input[-1] = temp

print(input)