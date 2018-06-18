#part1
class MathDojo1(object):
    def __init__(self):
        self.value = 0
    def add(self,*arg):
        a = sum(arg)
        self.value +=a
        return self
    def subtract(self, *arg):
        a = sum(arg)
        self.value -=a
        return self
    def result(self):
        return self.value
my_math = MathDojo1()
print(my_math.add(2).add(2,5).subtract(3,2).result())

#part2
class MathDojo2(object):
    def __init__(self):
        self.value = 0

    def add(self, *arg):
        a =0
        for e in arg:
            if type(e) is int:
                a +=e
            elif type(e) is list or tuple:
                a +=sum(e)

        print(a)
        self.value += a
        return self

    def subtract(self, *arg):
        a = 0
        for e in arg:
            if type(e) is int:
                a += e
            elif type(e) is list or  tuple:
                a += sum(e)
        print(a)
        self.value -= a
        return self

    def result(self):
        print(self.value)
my_math = MathDojo2()
my_math.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25],(1,2,3,4)).subtract(2, [2,3], [1.1,2.3]).result()