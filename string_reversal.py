a = "Robot Framework"
print(a[::-1])
print(reversed(a))

x = 'Hello World'
y = str("Hello World")
z = " ".join(x.split(" "))

print(z)
print(id(x), id(y), id(z))
print(x == y)
print(x is y)
print(x == z)
print(x is z)

arr = 'a', 2, 200.8
print(arr)
print(type(arr))
print(bool(()))
print(range(6))

for i in range(6): #same as for i in range(0, 6)
    print(i)

a = 1, 'Hi', 100.20
print(len(a))
print(len(str(a)))
print(str(a))
print(''.join(str(a).replace("'",'').replace('(','').replace(')','').split(', ')))

a = 'Hi'
b = 2
print(f"{a}{b:.2f}")

person = {"name": "Alice", "age": 30}
print(f"{person['name']} is {person['age']} years old.")