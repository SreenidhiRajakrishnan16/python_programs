def find_even(rang):
    even_nums = list()
    for i in range(rang):
        if(i%2 == 0):
            even_nums.append(i)
    print(even_nums)
    return even_nums

def any_number_of_args_find_even(*args):
    outer_even_nums = list()
    print(args)
    print(type(args))
    for x in args:
        # even_nums.clear() does not do the job because when inserted into outer_even_nums list and then cleared, outer_even_nums' item now points to the cleared even_nums list and then when new items are added to even_nums, outer_even_nums' member also changes to the new even_nums content as basically the same memory location(even_nums) get updated. So to overcome this a new even_nums list must be created each time.
        even_nums= []
        for i in range(x):
            if(i%2 == 0):
                even_nums.append(i)
        # print(even_nums)
        outer_even_nums.insert(args.index(x),even_nums)
        # print(outer_even_nums)
    print(outer_even_nums)
    return outer_even_nums

def find_even_between_range(end, start):
    even_nums = []
    for i in range(start, end):
        if(i%2 == 0):
            even_nums.append(i)
    print(even_nums)
    return even_nums

def find_even_between_multi_range(**kwargs):
    start = kwargs['start'] if 'start' in kwargs.keys() else 10
    end = kwargs['end'] if 'end' in kwargs.keys() else start+10
    print(start, end)
    even_nums = []
    for i in range(start, end):
        if(i%2 == 0):
            even_nums.append(i)
    print(even_nums)
    return even_nums

find_even(10)
any_number_of_args_find_even(10, 20)
find_even_between_range(start=10, end=20)
find_even_between_multi_range(start=10)
find_even_between_multi_range(start=40, end=70)