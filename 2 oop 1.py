
class Dog:
    type = 'aniaml'
    class_type = 'mammals'

    def __init__(self, name, age):
        self.n = name
        self.a = age

    def intro(self):
        print(f'dog name is {self.n} at age of {self.a}')

    def speak(self):
        print('haap hap')

    def __str__(self):
        return f'dog is {self.n} at {self.a}'


jessie = Dog('jessica', 2)

jessie.intro()

jessie.speak()

print(jessie)

print(jessie.type)

print(jessie.class_type)
