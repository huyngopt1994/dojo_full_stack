def test_argument(first, second, *args, **kwargs):
    print("This is first parameter %s" % first)
    print("This is second parameter %s" % second)
    print(args)
    print(kwargs)


test_argument(1,2,3,4,5,
              name='huy',
              age=14)