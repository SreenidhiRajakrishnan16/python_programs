class For:
    def __iter__(self):
        self.a = 2
        return self
    
    def __next__(self):
        if self.a < 20:             # 2, 5, 8, 11, 14, 17
            x = self.a              # 2, 5, 8, 11, 14, 17
            self.a = self.a+3       # 5, 8, 11, 14, 17, 20
            return x                # 2, 5, 8, 11, 14, 17
        else:
            raise StopIteration     # goes into infinite loop without raising StopIteration
        
    def __init__(self):
        self.a = 1
        # self.b = 2

cust_for = For()
for i in cust_for:
    pass
    print(i)
# print()


class Fib():
    def __iter__(self):
        self.a = 0
        self.b = 1
        self.count = 0
        return self
    
    def __next__(self):
        if self.count > 20:
            raise StopIteration
        val = self.a
        self.a = self.b
        self.b = val + self.b
        # or do in a single line self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return val

fib = Fib()
for i in fib:
    print(i)