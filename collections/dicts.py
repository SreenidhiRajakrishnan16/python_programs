dic = dict(name = 'Alice', place = 'Wonderland')

k = dic.keys()
print(k)

dic['production'] = 'Disney'
print(k)

s = {1,2,3}
s1 = {3,4,5}

s3 = s.union(s1)

s1.add(6)
print(s3)