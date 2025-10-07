x = "Hello World"                       #	str	
print(x)
print(type(x))
x = 20                                  #	int	
print(x)
print(type(x))
x = 20.5                                #	float	
print(x)
print(type(x))
x = 1j                                  #	complex	
print(x)
print(type(x))
x = ["apple", "banana", "cherry"]       #	list	
print(x)
print(type(x))
x = ("apple", "banana", "cherry")       #	tuple	
print(x)
print(type(x))
x = range(6)                            #	range	
print(x)
print(type(x))
x = {"name" : "John", "age" : 36}       #	dict	
print(x)
print(type(x))
x = {"apple", "banana", "cherry"}       #	set	
print(x)
print(type(x))
x = frozenset({"apple", "banana", "cherry"})                                    #	frozenset	
print(x)
print(type(x))
x = True                                #	bool	
print(x)
print(type(x))
x = b"Hello"                            #	bytes	
print(x)
print(type(x))
x = bytearray(5)                        #	bytearray	
print(x)
print(type(x))
x = memoryview(bytes(5))                #	memoryview	
print(x)
print(type(x))
x = None                                #   NoneType
print(x)
print(type(x))


# Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:

x = str("Hello World")                #	str	
print(x)
print(type(x))
x = int(20)                           #	int	
print(x)
print(type(x))
x = float(20.5)                       #	float	
print(x)
print(type(x))
x = complex(1j)                       #	complex	
print(x)
print(type(x))
x = list(("apple", "banana", "cherry"))        #	list	
print(x)
print(type(x))
x = tuple(("apple", "banana", "cherry"))       #	tuple	
print(x)
print(type(x))
x = range(6)                           #	range	
print(x)
print(type(x))
x = dict(name="John", age=36)          #	dict	
print(x)
print(type(x))
x = set(("apple", "banana", 1))                            #	set	
print(x)
print(type(x))
x = frozenset(("apple", "banana", "cherry"))                              #	frozenset	
print(x)
print(type(x))
x = bool(-1)                           #	bool	
print(x)
print(type(x))
x = bytes(5)                              #	bytes	
print(x)
print(type(x))
x = bytearray(5)                              #	bytearray	
print(x)
print(type(x))
x = memoryview(bytes(5))                              #	memoryview
print(x)
print(type(x))

#conversion
#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

a = str(1)
b = list('2')
print(b)
b = str(b)


print(a)
print(b)
print(type(b))
print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

x = int(float('4.2'))
y = float('4')
z = int('6')

print(x)
print(y)
print(z)

