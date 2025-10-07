print("a",2)
# print("{} {}".format("a"+ 2))
'''
Hi
'''
"""
Hello
"""
x = "Sally"
x = 2
x = str("Sally")
x = 2
print(type(x))

fruits = x, y, z = ['apple', 'orange', 'peach']
x, y, z = fruits
print(fruits)
print(type(fruits))
print(x)
print(y)
print(z)

x, y, z = 'a', "week", 3
print(x)
print(y)
print(z)

arr = x, y, z = ("a", 2, 3.0)
print(arr)
print(type(arr))
print(x)
print(y)
print(z)

x = 2
y = 5.0
print(x, y)
print(x+y)

x = str(2)
y = str(5)
print(x, y)
print(x+y)

x = 'Hello'
y = 'World'
print(x,y)
print(x+y)

x = 2
y = 'Hello'
print(x, y)
print(str(x) + y)

x = "aweseome"
y = "amazing"

def myFunc():
    print(x)
    # x = 'superb'
    global y
    y = "fantastic"
    print(x)
    print(y)

myFunc()
print(x)
print(y)

zx = list('apple')
zx = set('banana')
ax = dict(a= 'b', b ='c')
c = dict([('a', 'b')])
c = dict((('a', 'b')))
print(c)
# Output: {'a': 'b'}

print(c)
print(zx)