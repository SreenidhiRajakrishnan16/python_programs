# 💡 PYTHON SET – COMPLETE REFERENCE WITH OUTPUT COMMENTS

# 1️⃣ Creating sets
s = set()                               # Empty set
print(s)                                # set()
print(type(s))                          # <class 'set'>

s = {1, 2, 3, 4}
print(s)                                # {1, 2, 3, 4}

# ⚠️ Sets are unordered and contain unique elements only
s = {1, 2, 3, 2, 1, True, 0, False}     # False and 0 are considered dupes and so are True and 1 because they have the SAME HASH
print(s)                                # {False, 1, 2, 3} or ${0, 1, 2, 3}

# 2️⃣ Creating from iterables
s = set([1, 2, 3])
print(s)                                # {1, 2, 3}

s = set("banana")
print(s)                                # {'b', 'n', 'a'} (unordered, duplicates removed)

# 3️⃣ Uniqueness & mutability
s.add("apple")
print(s)                                # {'b', 'a', 'n', 'apple'}
# s[0] ❌ - TypeError: 'set' object is not subscriptable (no indexing or slicing)

# 4️⃣ Updating sets
s.update(["cherry", "mango"])
print(s)                                # {'a', 'apple', 'b', 'n', 'cherry', 'mango'}

# 5️⃣ Removing elements
s.remove("apple")
print(s)                                # {'a', 'b', 'n', 'cherry', 'mango'}
# s.remove("xyz") ❌ - KeyError if element not found
s.discard("xyz")                        # Safe: does nothing if missing
print(s)                                # {'a', 'b', 'n', 'cherry', 'mango'}
s.pop()                                 # Removes random element
print(s)                                # One element missing (random)
s.clear()                               # Remove all elements
print(s)                                # set()

# 6️⃣ Set from comprehension
s = {x for x in range(10) if x % 2 == 0}
print(s)                                # {0, 2, 4, 6, 8}

# 7️⃣ Mathematical set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))                       # {1, 2, 3, 4, 5, 6}
print(a | b)                            # {1, 2, 3, 4, 5, 6}

print(a.intersection(b))                # {3, 4}
print(a & b)                            # {3, 4}

print(a.difference(b))                  # {1, 2}
print(a - b)                            # {1, 2}

print(a.symmetric_difference(b))        # {1, 2, 5, 6}
print(a ^ b)                            # {1, 2, 5, 6}

# 8️⃣ Update in place
a = {1, 2, 3}
b = {3, 4}
a.update(b)
print(a)                                # {1, 2, 3, 4}

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a.intersection_update(b)
print(a)                                # {3, 4}

# 9️⃣ Membership tests
s = {'apple', 'banana', 'cherry'}
print('apple' in s)                     # True
print('mango' not in s)                 # True

# 🔟 Copying sets
s1 = {'apple', 'banana'}
s2 = s1.copy()
s1.add('cherry')
print(s1)                               # {'apple', 'banana', 'cherry'}
print(s2)                               # {'apple', 'banana'}

# 1️⃣1️⃣ Set relationships
x = {1, 2, 3}
y = {1, 2, 3, 4, 5}

print(x.issubset(y))                    # True
print(y.issuperset(x))                  # True
print(x.isdisjoint({7, 8}))             # True
print(x.isdisjoint({2, 8}))             # False

# 1️⃣2️⃣ Frozen sets (immutable version)
fs = frozenset([1, 2, 3])
print(fs)                               # frozenset({1, 2, 3})
# fs.add(4) ❌ - AttributeError: 'frozenset' object has no attribute 'add'

# 1️⃣3️⃣ Built-in functions
nums = {10, 20, 30, 40}
print(len(nums))                        # 4
print(min(nums))                        # 10
print(max(nums))                        # 40
print(sum(nums))                        # 100

# 1️⃣4️⃣ Conversions
nums = [1, 2, 2, 3, 3, 3]
unique = set(nums)
print(unique)                           # {1, 2, 3}

# Convert set back to list/tuple
print(list(unique))                     # [1, 2, 3]
print(tuple(unique))                    # (1, 2, 3)

# 1️⃣5️⃣ Iteration
fruits = {'apple', 'banana', 'cherry'}
for f in fruits:
    print(f)
# apple
# banana
# cherry

# 1️⃣6️⃣ Unpacking
a, b, c = {'apple', 'banana', 'cherry'}
print(a, b, c)
# apple banana cherry (order unpredictable)

# 1️⃣7️⃣ Set union of multiple sets
s1 = {1, 2}
s2 = {2, 3}
s3 = {3, 4}
print(set.union(s1, s2, s3))            # {1, 2, 3, 4}

# 1️⃣8️⃣ Intersection of multiple sets
print(set.intersection(s1, s2, s3))     # set() (no common elements)

# 1️⃣9️⃣ Using sets to remove duplicates
words = ["apple", "banana", "apple", "cherry", "banana"]
unique_words = list(set(words))
print(unique_words)                     # ['apple', 'banana', 'cherry'] (order arbitrary)

# 2️⃣0️⃣ Combining sets & comprehensions
fruits = {"apple", "banana", "cherry"}
filtered = {x.upper() for x in fruits if "a" in x}
print(filtered)                         # {'APPLE', 'BANANA'}

del(s)          # deletes the set altogether
print(s)        # NameError: name 's' is not defined