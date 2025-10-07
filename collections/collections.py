l = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
print(l[-5:-4])
l[1:3] = ['cica']
print(l)
l[1:3] = 'cica'
print(l)
l.insert(1, 'cica')
print(l)
l[1] = 'celery'
print(l)
m = ('orange', 'guava')
l.extend(m)
l.extend({'a', 1})
l.extend({'A': 1, 'V': 2})
print(l)

newlist = [x for x in range(10) if x < 5]
print(newlist)

l = ['apple', 'orange', 'banana', 'cherry', 'apple', 'kiwi', 'mango']
newlist1 = [x for x in l if x != 'apple' and 'a' in x]
print(newlist1)

newlist1 = [x if x != 'apple' else 'orange' for x in l]
print(newlist1)

l = [x for x in l if x != 'apple']
print(l)

ns = {x for x in range(10)}
print(ns)

fruits = ["apple", "banana", "cherry"]
basket = fruits       # basket points to the same list


fruits[:] = [x for x in fruits if x != "banana"]

print(fruits)  # ['apple', 'cherry']
print(basket)  # ['apple', 'cherry']   <- updated too!

fruits.reverse()
print(fruits)
print(basket)