# define e bool:

class Cart:
    def __init__(self, *args):
        self.items = list(args)

    def __bool__(self):
        return len(self.items) > 0

    def __add__(self, other):
        new_items = self.items + other.items
        return Cart(*new_items)

    def __getitem__(self, key):
        return self.items[key]

    def __setitem__(self, key, value):
        self.items[key] = value
        


c1 = Cart()
c2 = Cart('ketab', 'daftar')
print(bool(c1), bool(c2))

c3 = Cart('khodkar', 'madad')
c4 = c2 + c3
print(c4.items)
# add yani c1.__add__(c3)

# __sub__ __mul__ __div__ __add__

# vase indexe cart: __getitem__

print(c2[1], c2[0:2], sep='  ')

# vase c2[0]='pakkon' c2.__setitem__(0)='pakkon'
# albate tuple setitem nadare
# tu tuple + darim

c2[0] = 'pakkon'

print(c2.items)

