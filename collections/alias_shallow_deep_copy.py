
import copy

#ALIAS -> Same inner and outer list reference
print('ALIAS')
fruits = [['apple', 'banana'],['cherry'],'dragonfruit']

basket_alias = fruits  # both point to the same inner and outer lists -> changes to either will reflect to both fruits and basket_alias as they both point to one and the same object in memory

print(fruits) #[['apple', 'banana'], ['cherry'], 'dragonfruit']
print(basket_alias) #[['apple', 'banana'], ['cherry'], 'dragonfruit']

fruits[2] = 'dates'
basket_alias[0][0] = 'apricot'
print(fruits) #[['apricot', 'banana'], ['cherry'], 'dates']
print(basket_alias) #[['apricot', 'banana'], ['cherry'], 'dates']

#SHALLOW COPY using slicer : -> Creates a new outer list. Inner lists point to the same object
print('#SHALLOW COPY using slicer :')
fruits = [['apple', 'banana'],['cherry'],'dragonfruit']

basket_shallow = fruits[:] # creates a new outer list with the same inner list for both fruits and basket_shallow. Any changes to the inner list from either fruits or basket_shallow will affect both the lists' inner list. Any change to outer list will effect only that list. Leak happens only when the inner list mutates.

print(fruits) #[['apple', 'banana'], ['cherry'], 'dragonfruit']
print(basket_shallow) #[['apple', 'banana'], ['cherry'], 'dragonfruit']

fruits[2] = 'dates' # -> change reflects only in fruits
basket_shallow[0][0] = 'apricot' # -> change reflects in both fruits and basket_shallow because the inner list is shared
fruits[1][0] = 'cica' # -> change reflects in fruits and leaks basket_shallow as inner list is shared and points to the same object in memory
print(fruits) #[['apricot', 'banana'], ['cica'], 'dates']
print(basket_shallow) #[['apricot', 'banana'], ['cica'], 'dragonfruit']

#SHALLOW COPY using list() : -> Creates a new outer list. Inner lists point to the same object
print('#SHALLOW COPY using list() :')
fruits = [['apple', 'banana'],['cherry'],'dragonfruit']

basket_shallow = list(fruits) # creates a new outer list with the same inner list for both fruits and basket_shallow. Any changes to the inner list from either fruits or basket_shallow will affect both the lists' inner list. Any change to outer list will effect only that list. Leak happens only when the inner list mutates.

print(fruits) #[['apple', 'banana'], ['cherry'], 'dragonfruit']
print(basket_shallow) #[['apple', 'banana'], ['cherry'], 'dragonfruit']

fruits[2] = 'dates' # -> change reflects only in fruits
basket_shallow[0][0] = 'apricot' # -> change reflects in both fruits and basket_shallow because the inner list is shared
fruits[1][0] = 'cica' # -> change reflects in fruits and leaks basket_shallow as inner list is shared and points to the same object in memory
print(fruits) #[['apricot', 'banana'], ['cica'], 'dates']
print(basket_shallow) #[['apricot', 'banana'], ['cica'], 'dragonfruit']

#SHALLOW COPY using copy() -> Creates a new outer list. Inner lists point to the same object
print('#SHALLOW COPY using copy() :')
fruits = [['apple', 'banana'],['cherry'],'dragonfruit']

basket_shallow = fruits.copy() # creates a new outer list with the same inner list for both fruits and basket_shallow. Any changes to the inner list from either fruits or basket_shallow will affect both the lists' inner list. Any change to outer list will effect only that list. Leak happens only when the inner list mutates.

print(fruits) #[['apple', 'banana'], ['cherry'], 'dragonfruit']
print(basket_shallow) #[['apple', 'banana'], ['cherry'], 'dragonfruit']

fruits[2] = 'dates' # -> change reflects only in fruits
basket_shallow[0][0] = 'apricot' # -> change reflects in both fruits and basket_shallow because the inner list is shared
fruits[1][0] = 'cica' # -> change reflects in fruits and leaks basket_shallow as inner list is shared and points to the same object in memory
print(fruits) #[['apricot', 'banana'], ['cica'], 'dates']
print(basket_shallow) #[['apricot', 'banana'], ['cica'], 'dragonfruit']

#DEEP COPY -> Creates a new outer with new inner list. So no leak between variables
print('#Deep COPY')
fruits = [['apple', 'banana'],['cherry'],'dragonfruit']

basket_deep = copy.deepcopy(fruits) # creates a new outer list with a new inner list. Any change to outer/inner list from fruits will only affect fruits and any changes to inner/outer list from basket_deep will only affect basket_deep

print(fruits) #[['apple', 'banana'], ['cherry'], 'dragonfruit']
print(basket_deep) #[['apple', 'banana'], ['cherry'], 'dragonfruit']

fruits[2] = 'dates' # -> change reflects only in fruits as the inner list is old
basket_deep[0][0] = 'apricot' # -> change reflects in only in basket_deep as this inner list is a new one
fruits[1][0] = 'cica' # -> change reflects in only in fruits
print(fruits) #[['apple', 'banana'], ['cica'], 'dates']
print(basket_deep) #[['apricot', 'banana'], ['cherry'], 'dragonfruit']
