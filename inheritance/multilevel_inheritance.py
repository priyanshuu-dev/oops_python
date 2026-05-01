# multilevel_inheritance.py

class Car:
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")


class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand


class Fortuner(ToyotaCar):
    def __init__(self, brand, mileage):
        super().__init__(brand)  # parent constructor call
        self.mileage = mileage


# object creation
car1 = Fortuner("Toyota", 12)

print("Brand:", car1.brand)
print("Mileage:", car1.mileage)

car1.start()
        

