def isum(n):
    if n ==1:
        return n
    return isum(n-1) + n

print (isum(5))