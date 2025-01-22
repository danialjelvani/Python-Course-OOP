# mixin ye rahe beinabeine inheritance
# va compositione injur k multiple inheritance
# mishe ama ba ye functione moshakhase tekrari:
# behtare va mohem k hamishe tu tartibe inheritance
# class mixin ro aval biarim k complex nashe


class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2


class VolumeMixin:
    def volume(self):
        return self.area() * self.height


class Cube(VolumeMixin, Square):
    def __init__(self, length):
        super().__init__(length)
        self.height = 5


cu = Cube(3)
print(cu.area())
print(cu.volume())

# self.height ro mojaza tu har class tarif mikonimo
# besh migim
# self.area() ro hm tu har class ba function tarif mikonim
# va dar asl tu un mixin class tu init esh gheire self
# chizi nmiarim ta complex nashe va dg def __init__ barash nmiarim
