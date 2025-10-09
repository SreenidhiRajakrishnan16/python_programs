class Car:
    no_of_wheels = 4

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def print_details_of_inst(self):
        print(f'{self.brand}\'s {self.model} got released in {self.year}')
        print(f'Cars are {self.no_of_wheels}-wheelers')
        print(f'Cars are {Car.no_of_wheels}-wheelers')
        
    @classmethod
    def print_wheels(cls):
        print(f'All Cars are {cls.no_of_wheels}-wheeleers')
        print(f'All Cars are {Car.no_of_wheels}-wheeleers')

    @staticmethod
    def print_generic_details():
        print(f'Cars are a basic necessity in 2025')
        print(f'Cars have {Car.no_of_wheels+1} wheels if you consider stepney')
    
c1 = Car('Maruti', 'Alto', '2005')
print(f'{"Instance Method Print Statements":^50}')
c1.print_details_of_inst()
print(f'{"Class Method Print Statements":^50}')
c1.print_wheels()
print(f'{"Static Method Print Statements":^50}')
c1.print_generic_details()