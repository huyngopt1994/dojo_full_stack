def print_line(index=1, special_char=False):
    my_list = [str(x*int(index)) for x in range(1, 13)]
    if special_char:
        index = 'x'
    my_list.insert(0, str(index))
    print(' '.join(my_list))

print_line(special_char=True)
for i in range(1, 13):
    print_line(i)
