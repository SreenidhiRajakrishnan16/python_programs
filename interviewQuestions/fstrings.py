# f-strings demo: all major use cases

name = "Alice"
age = 30
pi = 3.1415926535
items = ["apple", "banana", "cherry"]

# 1️⃣ Basic interpolation
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Alice and I am 30 years old.

# 2️⃣ Expressions inside f-strings
print(f"In 5 years, {name} will be {age + 5} years old.")
# Output: In 5 years, Alice will be 35 years old.

# 3️⃣ Calling functions inside f-strings
def greet(person):
    return f"Hello, {person}!"
    #same as return "Hello, "+person

print(f"Function call inside f-string → {greet(name)}")
# Output: Function call inside f-string → Hello, Alice!

# 4️⃣ Accessing list, dict, or object attributes
person = {"name": "Alice", "age": 30}
print(f"{person['name']} is {person['age']} years old.")
# Output: Alice is 30 years old.

class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

my_car = Car("Tesla", 120)
print(f"My {my_car.brand} drives at {my_car.speed} km/h.")
# Output: My Tesla drives at 120 km/h.

# 5️⃣ Formatting numbers
print(f"Pi rounded to 2 decimals: {pi:.2f}")
# Output: Pi rounded to 2 decimals: 3.14

print(f"Pi with 5 total width and 3 decimals: {pi:5.3f}")
# Output: Pi with 5 total width and 3 decimals: 3.142

print(f"Large number with commas: {123456789:,}")
# Output: Large number with commas: 123,456,789

print(f"Percentage: {0.25:.2%}")
# Output: Percentage: 25.00%

# 6️⃣ Aligning and padding
print(f"|{'left':<10}|{'center':^10}|{'right':>10}|")
# Output: |left      |  center  |     right|

print(f"Binary: {42:b}, Hex: {42:x}, Octal: {42:o}")
# Output: Binary: 101010, Hex: 2a, Octal: 52

# 7️⃣ Debugging (Python 3.8+ feature)
print(f"{name}, {age}, {pi:.3f}")
# Output: Alice, 30, 3.142
print(f"{name=}, {age=}, {pi=:.3f}")
# Output: name='Alice', age=30, pi=3.142

# 8️⃣ Multiline f-strings
message = f"""
Hi {name},
You have {len(items)} items: {', '.join(items)}.
Your favorite number is approximately {pi:.2f}.
"""
print(message)
# Output:
# Hi Alice,
# You have 3 items: apple, banana, cherry.
# Your favorite number is approximately 3.14.

# 9️⃣ Nested f-string example (less common but possible)
status = f"User: {name.upper()} ({age})"
print(status)
# Output: User: ALICE (30)
status = f"User: {f'{name.upper()} ({age})'}"
print(status)
# Output: User: ALICE (30)