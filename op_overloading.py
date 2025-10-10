class Add3():
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a + 3
    
    def __str__(self):
        return f'Special Add 3 for 6 -> {self.a}'
    
num1 = Add3(6)
num2 = Add3(9)

print(num1 + num2)


class Vector():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, others):
        return Vector(self.a + others.a, self.b + others.a)
    
    def __repr__(self):
        return f'Vector {self.a}, {self.b}'
    
v1 = Vector(2, 3)
v2 = Vector(4, 5)

v3 = v1 + v2

print(v1)
print(v2)
print(v3)
