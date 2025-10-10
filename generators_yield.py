def cust_for(limit):
    a = 2
    while a < limit:
        yield a
        a += 3

for i in cust_for(20):
    # print(i)
    pass

def fib(limit):
    a, b = 0, 1
    count = 0
    while count <= limit:
        yield a
        a, b = b, a+b
        count += 1

for a in fib(20):
    print(a)