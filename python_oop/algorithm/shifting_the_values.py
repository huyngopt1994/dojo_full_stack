#shift from left to right , and set the last value to zero
def shifting(value):
    for i in range(1,len(value)):
        value[i-1] = value[i]

    value[-1] = 0
    return value
print(shifting([1,5, 10, 7, -2]))
