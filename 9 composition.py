# vs inheritance e
# horse IS AN aniaml = inheritance
# horse HAS A tail = composition
# if A is B and B is A its not good to use inheritance

class Color:
    def __init__(self, name, hex_code, rgb):
        self.name = name
        self.hex_code = hex_code
        self.rgb = rgb

    def __str__(self):
        return f'{self.name}  {self.hex_code} {self.rgb}'


c = Color('blue', '88aeeb', (136, 174, 235))


class Shape:
    def __init__(self, color):
        self.color = color


s = Shape(c)
print(s.color)
