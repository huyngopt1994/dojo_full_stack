input = [-3,5,1,3,2,10]

for i in range(0,len(input)//2+1):
    temp = input[0+i]
    input[0+i] = input[-1-i]
    input[-1-i] = temp

print (input)