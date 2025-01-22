class Point:
    def __init__(self, *args):
        self.args = args

    def __add__(self, other):
        args = map(sum, zip(self.args, other.args))
        return Point(*args)

    def __str__(self):
        return f'{self.__class__.__name__}{self.args}'


p1 = Point(1, 3)
p2 = Point(2, 2)

# sade shodash mmishe jame 2 ta tuple k ba zip
# michinim kenare hm k chon generatore list minevisim
# zip har tedad k bashe i-th ro ba i-th michine kenare ham
# from itertoold impor zip_longest ino age biarim mishe agr
# ye list bolantar bud besh default value dad

t1 = (1, 3)
t2 = (2, 2)

print(list(zip(t1, t2)))
print(list(map(lambda x: x[0]+x[1], zip(t1, t2))))
# or
print(list(map(sum, zip(t1, t2))))

print(p1 + p2 + p2)