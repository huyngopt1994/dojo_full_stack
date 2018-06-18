input = [1.5,10, -2]
sum =0
max = input[0]
min = input[0]
for i in input:
    if i >max:
        max = i
    if i < min:
        min = i

    sum += i

print (max)
print (min)
print (sum/len(input))
