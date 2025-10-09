class Demo:
    class_msg = 'Class Message'

    def __init__(self, brand, modelyear):
        self.brand = brand
        self.modelyear = modelyear

    # Instance Method
    def print_func_ins(self, msg):
        print('Instance Method printing Class attribute through self', msg, self.class_msg)
        print('Instance Method printing Instance attribute through self')
        print('Brand:', self.brand)
        print('Model:', self.modelyear)

    # Class Method
    @classmethod
    def print_func_cls(cls, msg):
        print('Class Method printing Class attribute through cls', msg, cls.class_msg)
        print('Class Method CANNOT access Instance attribute')

    # Static Method
    @staticmethod
    def print_func_static(msg):
        print('Static Method printing Class attribute through classname', msg, Demo.class_msg)
        print('Static Method CANNOT access Instance or Class attributes as it does not have access to self or cls', msg, Demo.class_msg)


d = Demo('Maruti', 'Alto')
print(type(d))

d.print_func_ins('- Called from Obj')
d.print_func_cls('- Called from Obj')
d.print_func_static('- Called from Obj')

# Demo.print_func_ins('- Called from classname')
Demo.print_func_cls('- Called from classname')
Demo.print_func_static('- Called from classname')

