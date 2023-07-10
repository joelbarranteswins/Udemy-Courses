class Vehicle():
    def __init__(self, color: str, wheel: str):
        self.color = color
        self.wheel = wheel
    
    def __str__(self):
        return f'{self.__class__.__name__}: {self.color} and {self.wheel}'

class Car(Vehicle):
    def __init__(self, color: str, wheel: str, velocity: int):
        assert type(velocity) in [int, float], 'velocity has to be int or float'
        Vehicle.__init__(self, color=color, wheel=wheel)
        self.velocity = velocity

    def __str__(self):
        return f'{self.__class__.__name__}: {self.color} y {self.wheel} with {self.velocity} (Km/h)'

class Bicycle(Vehicle):
    def __init__(self, color: str, wheel: str, type_vehicle: str):
        assert type_vehicle in ['urban', 'mountain', 'runner'], 'it has to be one type'
        Vehicle.__init__(self, color=color, wheel=wheel)
        self.type_vehicle = type_vehicle

    def __str__(self):
        return f'{self.__class__.__name__}: dolor:{self.color} and {self.wheel} with type {self.type_vehicle}'

if __name__ == '__main__':
    vehicle_1 = Vehicle(color='red', wheel='huge')
    print(vehicle_1)
    
    vehicle_2 = Car(color='blue', wheel='small', velocity=16)
    print(vehicle_2)

    vehicle_3 = Bicycle(color='orange', wheel='big', type_vehicle='urban')
    print(vehicle_3)

