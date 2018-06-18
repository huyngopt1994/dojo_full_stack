def ifactorial(n):
    if n ==1:
        return n
    return ifactorial(n-1)*n

print (ifactorial(5))