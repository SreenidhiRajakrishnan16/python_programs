a = 'Hello World! Here to Slay'
remove_vowels = str.maketrans('','','aeiou')
print(a.translate(remove_vowels))

remove_vowels_dict = str.maketrans({'a':None, 'e':None, 'i':None, 'o':None, 'u':None})
print(a.translate(remove_vowels_dict))

vowels = 'aeiou'
for ai in a:
    if(ai in vowels):
        a = a.replace(ai,'')
print(a)