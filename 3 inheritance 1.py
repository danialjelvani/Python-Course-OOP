
class Shape:
    def __init__(self, color=None):
        self.color = color


class Rectangle(Shape):
    def __init__(self, length, width, color=None):
        self.length = length
        self.width = width
        super().__init__(color)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


r = Rectangle(4, 2)
print(r.area(), r.perimeter(), sep='  ')
print(r.color)
# Single Inheritance:


class square(Rectangle):
    def __init__(self, length, color=None):
        super().__init__(length, length)
        self.length = length
        self.width = length


s = square(5)

print(f'{s.area():<2} {s.perimeter()}')
print(s.color)

# rahe dovom:


class Square2(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


s2 = Square2(6)


print(s2.area())
print(s2.width)
print(s2.color)


class Cube(Square2):
    def surface_area(self):
        surface = super().area()
        return surface * 6

    def volume(self):
        surface = super().area()
        return surface * self.length

# multilevel Inheritance:


c = Cube(3)
print(c.surface_area(), c.volume())
print(c.color)

# Haierarchial Inheritance:


class Circle(Shape):
    def __init__(self, radius, color):
        self.radius = radius
        super().__init__(color)

    def area(self):
        return self.radius ** 2 * 3.14

    def perimeter(self):
        return self.radius * 2 * 3.14


ci = Circle(3, 'red')

print(ci.area(), ci.perimeter(), ci.color)

print()

print(isinstance(ci, Circle))
print(isinstance(ci, Shape))
print(isinstance(ci, Rectangle))
print(isinstance(c, Rectangle))
print(isinstance(c, Square2))
print()
print(issubclass(Cube, Shape))
print(issubclass(Circle, Rectangle))
print(issubclass(Shape, Shape))
print(issubclass(Shape, object))
print()
print(issubclass(type, object))
print(isinstance(object, type))
