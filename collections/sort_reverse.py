nums = [3,1,4,2]
print(sorted(nums))
print(sorted(nums, reverse=True))

fruits = ['apple', 'cica', 'Banana', 'dates']
print(sorted(fruits))
print(sorted(fruits, key=str.lower))
fruits = ['apple', 'cica', 'Banana', 'dates']
print(sorted(fruits, reverse=True))
print(sorted(fruits, reverse=True, key=str.lower))