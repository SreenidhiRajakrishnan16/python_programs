class Car:
    no_of_wheels = 4

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
c1 = Car('Maruti', 'Alto')
print(c1.model)
print(c1.no_of_wheels)
print(c1.__dict__)
c1.no_of_wheels = 5
print(Car.no_of_wheels)
print(c1.no_of_wheels)
print(c1.brand)
print(c1.__dict__)