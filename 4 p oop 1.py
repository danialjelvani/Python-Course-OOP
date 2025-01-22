
class Vehicle:
    def __init__(self, max_speed, mileage, capacity):
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 10


class Bus(Vehicle):
    def fare(self):
        return super().fare() * 1.1


tesla = Vehicle(320, 660, 4)
school_bus = Bus(120, 300, 30)

print(school_bus.fare())
