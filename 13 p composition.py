# parent child:

class Human:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def speak(self, text):
        return f'{self.first_name} says: {text}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Parent(Human):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.kids = []

    def have_child(self, child_name):
        child = Child(self, child_name)
        self.kids.append(child)
        return child


class Child(Human):
    def __init__(self, parent, first_name):
        super().__init__(first_name, parent.last_name)
        self.parent = parent


p = Parent('danial', 'jelvani')
print(p.speak('hi'))
p.have_child('nini')
print(p)
print(p.kids)
c = Child(p, 'nini2')
print(p.kids)
