# 💡 PYTHON LIST – COMPLETE REFERENCE WITH OUTPUT COMMENTS

# 1️⃣ Creating lists
l = []                                 # Empty list
print(l)                               # []
print(type(l))                         # <class 'list'>

l = ['apple', 'banana', 'cherry']
print(l)                               # ['apple', 'banana', 'cherry']

mixed = [1, "apple", 3.14, True]
print(mixed)                           # [1, 'apple', 3.14, True]

# 2️⃣ Indexing and slicing
print(l[0])                            # apple
print(l[-1])                           # cherry
print(l[1:3])                          # ['banana', 'cherry']
print(l[-5:-4])                        # ['apple']

# 3️⃣ Changing values
l[1:3] = ['cica']
print(l)                               # ['apple', 'cica']
l[1:3] = 'cica'                        # Replaces elements one by one (iterable)
print(l)                               # ['apple', 'c', 'i', 'c', 'a']
l.insert(1, 'cica')                    # Insert without replacing
print(l)                               # ['apple', 'cica', 'c', 'i', 'c', 'a']
l[1] = 'celery'                        # Replace item at index 1
print(l)                               # ['apple', 'celery', 'c', 'i', 'c', 'a']

# 4️⃣ Adding elements
m = ('orange', 'guava')
l.extend(m)                            # Extend with a tuple
l.extend({'a', 1})                     # Extend with a set (unordered)
l.extend({'A': 1, 'V': 2})             # Extend with a dict (keys only)
print(l)
# Example output (unordered for sets):
# ['apple', 'celery', 'c', 'i', 'c', 'a', 'orange', 'guava', 1, 'a', 'A', 'V']

# 5️⃣ List comprehension
newlist = [x for x in range(10) if x < 5]
print(newlist)                         # [0, 1, 2, 3, 4]

l = ['apple', 'orange', 'banana', 'cherry', 'apple', 'kiwi', 'mango']
newlist1 = [x for x in l if x != 'apple' and 'a' in x]
print(newlist1)                        # ['orange', 'banana', 'mango']

newlist1 = [x if x != 'apple' else 'orange' for x in l]
print(newlist1)
# ['orange', 'orange', 'banana', 'cherry', 'orange', 'kiwi', 'mango']

# Remove all 'apple'
l = [x for x in l if x != 'apple']
print(l)                               # ['orange', 'banana', 'cherry', 'kiwi', 'mango']

# 6️⃣ Set comprehension
ns = {x for x in range(10)}
print(ns)                              # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# 7️⃣ Reference vs Copy
fruits = ["apple", "banana", "cherry"]
basket = fruits                        # basket points to same list
fruits[:] = [x for x in fruits if x != "banana"]
print(fruits)                          # ['apple', 'cherry']
print(basket)                          # ['apple', 'cherry'] (updated too!)

# 8️⃣ Reverse
fruits.reverse()
print(fruits)                          # ['cherry', 'apple']
print(basket)                          # ['cherry', 'apple']

# 9️⃣ Simple iteration
[print(x) for x in fruits]
# cherry
# apple

# 1️⃣0️⃣ Nested comprehension example
alist = [alist for alist in fruits if 'a' in alist]
print(alist)                           # ['apple']
[print(a_list) for a_list in fruits if 'a' in a_list]
# apple

# 1️⃣1️⃣ Conditional transformation
fruits = ['apple', 'Guava', 'Banana', 'cica']
newlist = [x if x != 'banana' else 'orange' for x in fruits]
print(newlist)
# ['apple', 'Guava', 'Banana', 'cica'] (unchanged because 'Banana' != 'banana')

# 1️⃣2️⃣ Sorting
print(sorted(fruits, key=len))         # Sort by string length
# ['cica', 'apple', 'Guava', 'Banana']
print(sorted(fruits))                  # Case-sensitive sort
# ['Banana', 'Guava', 'apple', 'cica']
print(sorted(fruits, key=str.lower))   # Case-insensitive sort
# ['apple', 'Banana', 'cica', 'Guava']

# 1️⃣3️⃣ List multiplication & concatenation
print(fruits * 3)
# ['apple', 'Guava', 'Banana', 'cica', 'apple', 'Guava', 'Banana', 'cica', 'apple', 'Guava', 'Banana', 'cica']

fruiten = fruits + fruits
print(fruiten)
# ['apple', 'Guava', 'Banana', 'cica', 'apple', 'Guava', 'Banana', 'cica']

# 1️⃣4️⃣ Converting iterables to lists
print(list("Hello"))                  # ['H', 'e', 'l', 'l', 'o']

# 1️⃣5️⃣ Common list methods
nums = [5, 1, 8, 3]
nums.append(10)
print(nums)                           # [5, 1, 8, 3, 10]
nums.insert(2, 99)
print(nums)                           # [5, 1, 99, 8, 3, 10]
nums.remove(1)
print(nums)                           # [5, 99, 8, 3, 10]
popped = nums.pop()
print(popped)                         # 10
print(nums)                           # [5, 99, 8, 3]
nums.sort()
print(nums)                           # [3, 5, 8, 99]
nums.reverse()
print(nums)                           # [99, 8, 5, 3]
print(nums.index(8))                  # 1
print(nums.count(5))                  # 1
nums.clear()
print(nums)                           # []

# 1️⃣6️⃣ Copying lists properly
a = ['apple', 'banana', 'cherry']
b = a.copy()                          # Creates a true copy
a.append('dragonfruit')
print(a)                              # ['apple', 'banana', 'cherry', 'dragonfruit']
print(b)                              # ['apple', 'banana', 'cherry']

# 1️⃣7️⃣ Nested lists
nested = [[1, 2], [3, 4], [5, 6]]
print(nested[0])                      # [1, 2]
print(nested[1][1])                   # 4

# 1️⃣8️⃣ Iterating nested lists
for sub in nested:
    for item in sub:
        print(item, end=' ')
# 1 2 3 4 5 6

# 1️⃣9️⃣ List comprehension with nested lists
flattened = [item for sub in nested for item in sub]
print(flattened)                      # [1, 2, 3, 4, 5, 6]

# 2️⃣0️⃣ min, max, sum
nums = [5, 10, 15]
print(min(nums))                      # 5
print(max(nums))                      # 15
print(sum(nums))                      # 30

del(nums)          # deletes the list altogether
print(nums)        # NameError: name 'nums' is not defined