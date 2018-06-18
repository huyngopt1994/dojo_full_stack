#try to create sorted and unsorted part
# try to move from unsorted to sorted part for per element
# pseudo code :
'''
for i = 1 to n -1:
    element = array[i]
    j = i
    while (j>0 and array[j-1]  > element )
        # ok we can move element => to the left
        array[j] = array[j-1]
        j = j -1 
    array[j-1]=  element

'''

for insetion