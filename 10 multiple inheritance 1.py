# right pyramid area:

class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

    def perimeter(self):
        return self.length * 4


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def triangle_area(self):
        return self.base * self.height * 0.5


class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        super().__init__(base)

    def area(self):
        base_area = super().area()
        perimeter_area = super().perimeter() * self.slant_height / 2
        pyramid_area = base_area + perimeter_area
        return pyramid_area


p = RightPyramid(2, 4)

# methoc resolution order ya MRO mige k ba che tartibi
# mire soraghe parenta:

print(RightPyramid.__mro__)

# tu in mesal aval mire soraghe triangle agr
# tu parentinge rightpyramid aval triangle ro benevisim
# vase inke in etefagha pish nayad esme functiona har
# class motefavet bashe

print(p.area())

# kolan kheili sakht mishe chon khodesh
# tebghe MRO mire jelo va sakhtaraz hame mogheye
# parameter grftn function az pedare
