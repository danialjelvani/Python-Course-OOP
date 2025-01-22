# point class:
# agar dar str chizi nabashe mire repr ro seda mmizne:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#    def __str__(self):
#       return f'{self.__class__.__name__}({self.x},{self.y})'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x},{self.y})'

    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5

    def __lt__(self, obj):
        return abs(self) < abs(obj)


p1 = Point(3, 4)
print(p1)
print(abs(p1))

my_points = [Point(3, 4), Point(9, 9), Point(6, 8), Point(1, 10)]

# sort:
# on^2 hast in olgoo payin


def sort_list(l_source):
    l = l_source.copy()
    for _ in range(len(l)):
        for ind in range(len(l) - 1):
            if l[ind + 1] < l[ind]:
                l[ind], l[ind + 1] = l[ind + 1], l[ind]
    return l


def sort_list_abs(l_source):
    l = l_source.copy()
    for _ in range(len(l)):
        for ind in range(len(l) - 1):
            if abs(l[ind + 1]) < abs(l[ind]):
                l[ind], l[ind + 1] = (l[ind + 1]), l[ind]
    return l


my_points2 = [3, 6, 9, 2, 8, 1]
print(sort_list(my_points2))
print(sort_list_abs(my_points))


# moghayese beine point ha error midad b hamin khater
# umdim tu function __lt__ tu class tarifesh krdim
# __lt__   :   lesser than
# __gt__   :   greater than
# __le__   :   lesser equal
# __ge__   :   greater equal
print(sort_list(my_points))

# khate payin b rahati hame karo mikone dg ba tarife mojadade less than
print(sorted(my_points))

# sort bar asas y e points
print(sorted(my_points, key=lambda p: p.y))

# sort bar asas abs e point ham mishe:
print(sorted(my_points, key=lambda p: abs(p)))
