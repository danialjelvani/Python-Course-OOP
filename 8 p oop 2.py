# tu n dimension:

class Point:
    def __init__(self, *args):
        self.vector = args
        print(len(self.vector))

    def __repr__(self):
        return f'{self.__class__.__name__}{self.vector}'

    def __abs__(self):
        sum = 0
        for x in self.vector:
            sum += x**2
        return sum**0.5

    def __lt__(self, obj):
        return abs(self) < abs(obj)


p = Point(3, 4, 5, 8, 9, 9, 91)
print(p)
print(abs(p))

my_points = [Point(2, 2, 2, 2), Point(20, 30), Point(11, 18, 3), Point(60)]
print(sorted(my_points))

# or

print(sorted(my_points, key=lambda p: abs(p)))
