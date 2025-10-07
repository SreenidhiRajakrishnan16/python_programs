import re
x = "Hello, World"
print(x[1])

x = '''Hello
There'''
for i in x:
    print(i)

print('Hello' in x)
print('Hello' not in x)

if ('Hello' in x):
    print(True)

if('There' not in x):
    print(False)

if 'Hello' in x:
    print(True)

if 'There' not in x:
    print(False)

a = "Hello World"
print(a[2:5])
print(a[2:])
print(a[:5])
print(a[-1])
print(a[-4:-1])

a.upper()
print(a)
print(a.upper())


c = "hello" + str(2)
print(c)

price = 20
print(float(2))
a = 'hello'
c = f"{a} {2}"
print(c)

quantity = 10
price = 20
print(f"Total quantity is {quantity}")
print(f"Total price is {price * quantity}")
print(f"Total price in decimals {price * quantity: .2f}")

txt = 'hellp\rworld'
print(txt)
print("hello\rhi")
print("hello\nworld")
print('hello\bworld')

a = 'hello\tthereo'
print(a.capitalize())
print(a.casefold())
print(a.center(50))
print(a.count('e'))
print(a.encode("utf-8"))
print(a.endswith('o'))
print(a.expandtabs(5))
print(a.find('o'))
print(a.format())
# print(a.format_map())
print(a.index('l'))
print(a.title().istitle())
arr = ["apple", "costs", '200', 'Rs. per Kg.']
print(" ".join(arr))
print(arr[0].ljust(20), " ".join(arr))
print("   Hello World  ".strip())
x = 'hello world'

translation_map = str.maketrans({'h': 't',
                                 'a': '1'})
print(x.translate(translation_map))
print(x.rpartition('hello'))
print(x.rfind('lo'))
print(x.rindex('lo'))
print('hello w'.zfill(10))

print('hello'.partition('hello'))
print('hello'.rpartition('hello'))

x = 'hello - world - hi - there'
print(x.split('-', 3))
print(x.rsplit('-', 3))
# print(x.split())
print(x.partition('-'))
print(x.rpartition('-'))

print('2myvar'.isidentifier())
print('-myvar'.isidentifier())
print('_myvar'.isidentifier())
print('class'.isidentifier())
print('def'.isidentifier())

print(x)
print(x.replace('-','*'))
trans = str.maketrans('-','*')
print(x.translate(trans))

o2otrans = str.maketrans('abc','efg', 'xy')
o2mtrans = str.maketrans({'a':'abc', 'd':''})
print('abcdefghixyz'.translate(o2otrans))
print('abcdefghi'.translate(o2mtrans))

print(re.sub(r"\d", '*', 'abcd123'))
print(bool(1*0))

n = 999
if n >100 | n<1000:
    print(n)
print(5/3)
print(5//3)

x = 10**300
y = 10**300
print(x==y)
print(x is y)

z = 10**300
print(x == z)
print( x is z)
print("hello" == "he"+"llo")
print("hello" is "he"+"llo")

a = "".join(["he", "llo"])
b = "hello"

print(a == b)  # True → values match
print(a is b)

x= 5
x = +x 
x **=x

# while (line := input("Enter: ")) != "quit":
#     print("You typed:", line)

import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN, ROUND_HALF_EVEN
nums = []
for i in range(20):
    r = math.sqrt(i)
    if (r:= math.sqrt(i)).is_integer():
        nums.append(int(i))
print(nums)
print(math.sqrt(20))
print(int(math.sqrt(20)) + 1)
print(Decimal(4.5).to_integral_value(rounding=ROUND_HALF_UP))
print(Decimal(4.5).to_integral_value(rounding=ROUND_HALF_DOWN))
print(Decimal(4.5).to_integral_value(rounding=ROUND_HALF_EVEN))

print(math.ceil(4.1))