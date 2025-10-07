# 💡 PYTHON TUPLE – COMPLETE REFERENCE WITH OUTPUT COMMENTS

# 1️⃣ Creating tuples
tup1 = ()                         # Empty tuple
print(tup1)                       # ()
print(type(tup1))                 # <class 'tuple'>

tup2 = (1, 2, 3)
print(tup2)                       # (1, 2, 3)

tup3 = 'a', 'b', 'c'              # Parentheses optional
print(tup3)                       # ('a', 'b', 'c')

tup4 = ('a',)                     # Single-element tuple → needs comma
print(tup4)                       # ('a',)
print(type(tup4))                 # <class 'tuple'>

tup5 = ('a')                      # ❌ Not a tuple
print(tup5)                       # a
print(type(tup5))                 # <class 'str'>

# 2️⃣ Tuple immutability
tup = (1, 2, 3)
# tup[0] = 10                     # ❌ TypeError: 'tuple' object does not support item assignment
print(tup)                        # (1, 2, 3)

# ✅ To modify a tuple → convert to list → modify → convert back
tup = (1, 2, 3)
temp_list = list(tup)             # Convert tuple to list
temp_list.append(4)               # Modify
temp_list[0] = 99                 # Update value
tup = tuple(temp_list)            # Convert back to tuple
print(tup)                        # (99, 2, 3, 4)

# 3️⃣ Tuple indexing and slicing
tup = ('apple', 'banana', 'cherry', 'date', 'fig')
print(tup[0])                     # apple
print(tup[-1])                    # fig
print(tup[1:4])                   # ('banana', 'cherry', 'date')
print(tup[:3])                    # ('apple', 'banana', 'cherry')
print(tup[::2])                   # ('apple', 'cherry', 'fig')

# 4️⃣ Tuple concatenation and repetition
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)                    # (1, 2, 3, 4)
print(t1 * 3)                     # (1, 2, 1, 2, 1, 2)

# 5️⃣ Membership test
tup = ('apple', 'banana', 'cherry')
print('apple' in tup)             # True
print('grape' not in tup)         # True

# 6️⃣ Tuple methods
tup = ('apple', 'banana', 'cica', 'banana', 'apple', 'cica')
print(tup.count('apple'))         # 2
print(tup.index('banana'))        # 1

# 7️⃣ Tuple unpacking
tup = ('apple', 'banana', 'cherry')
a, b, c = tup
print(a)                          # apple
print(b)                          # banana
print(c)                          # cherry

# Extended unpacking with *
tup = ('apple', 'banana', 'cherry', 'date', 'fig')
a, *b = tup
print(a)                          # apple
print(b)                          # ['banana', 'cherry', 'date', 'fig']

a, b, *c = tup
print(a)                          # apple
print(b)                          # banana
print(c)                          # ['cherry', 'date', 'fig']

a, *b, c = tup
print(a)                          # apple
print(b)                          # ['banana', 'cherry', 'date']
print(c)                          # fig

# 8️⃣ Tuple nesting
nested = (1, (2, 3), (4, 5, 6))
print(nested[1])                  # (2, 3)
print(nested[1][0])               # 2

# 9️⃣ Tuple with mixed data types
mixed = (1, "apple", 3.14, True)
print(mixed)                      # (1, 'apple', 3.14, True)
print(type(mixed[2]))             # <class 'float'>

# 🔟 Tuple from iterables, String
tup_from_list = tuple([1, 2, 3])
print(tup_from_list)              # (1, 2, 3)

tup_from_str = tuple("abc")
print(tup_from_str)               # ('a', 'b', 'c')

# 1️⃣1️⃣ Tuple length
print(len(tup_from_list))         # 3

# 1️⃣2️⃣ Tuple comparison
t1 = (1, 2, 3)
t2 = (1, 2, 4)
print(t1 < t2)                    # True
print(t1 == (1, 2, 3))            # True

# 1️⃣3️⃣ Tuple in loops
tup = ('apple', 'banana', 'cherry')
for fruit in tup:
    print(fruit)
# apple
# banana
# cherry

# 1️⃣4️⃣ Tuple comprehension alternative (generator)
# Tuples don’t have their own comprehension syntax, but you can use parentheses
# This actually creates a generator, not a tuple directly
gen = (x.upper() for x in ('apple', 'banana'))
print(gen)                        # <generator object ...>
print(tuple(gen))                 # ('APPLE', 'BANANA')

# ⚡ Note:
# List comprehension uses [] → creates a list immediately
# Tuple "comprehension" uses () → creates a generator (lazy sequence)

# 1️⃣5️⃣ Tuple unpacking in loops
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
for num, letter in pairs:
    print(num, letter)
# 1 a
# 2 b
# 3 c

# 1️⃣6️⃣ Tuple immutability caveat (mutable inside)
tup = (1, [2, 3])
tup[1].append(4)                  # The list inside can still be modified
print(tup)                        # (1, [2, 3, 4])

# 1️⃣7️⃣ Tuple packing and unpacking
a, b = 10, 20
tup = a, b
print(tup)                        # (10, 20)

a, b = tup
print(a, b)                       # 10 20

# 1️⃣8️⃣ Tuple as dictionary key (hashable)
locations = {("Paris", "France"): 48.8566, ("Tokyo", "Japan"): 35.6762}
print(locations[("Paris", "France")])  # 48.8566

# 1️⃣9️⃣ Built-in functions
nums = (10, 20, 30, 40)
print(min(nums))                  # 10
print(max(nums))                  # 40
print(sum(nums))                  # 100

# 2️⃣0️⃣ Sorting tuples
tup = (3, 1, 4, 2)
print(sorted(tup))                # [1, 2, 3, 4]
print(tuple(sorted(tup)))         # (1, 2, 3, 4)

del(tup)          # deletes the tuple altogether
print(tup)        # NameError: name 'tup' is not defined