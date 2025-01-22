# function dir hame method hae ye objecto neshun mide

a = (1, 2, 3, 40)

for x in dir(a):
    print(x)

# a[x] hamoon a.__getitem__(x) e

print()


class Cart:
    def __init__(self, *args, customer_name):
        self.items = args
        self.customer = customer_name

    def __len__(self):
        return len(self.items)


# agar be customer_name bala meghdar default bedim dg moghe call e function
# elzami b dadn customer_name nis va hamero mirize tu args va
# customer_name hamun default mimune ama age meghdar default nadim
# elzam mikone moghe call e function k bgimesh


c1 = Cart('khodkar', 'daftar', 'ketab', customer_name='ali')
print(c1.customer)
print(len(c1))
