# abstract method yek rahe force krdne
# class hast kye funtionio tarif konan
# masalan force mikonim k hame class haye shape
# area o premeter dashte bashan:
# in kar nazm mide va majbur mikone ye olgoo ro
# edameh bede barnameh 


from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color='black'):
        self.color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def area(self):
        return super().area()

    def perimeter(self):
        return super().perimeter()


r = Rectangle()
