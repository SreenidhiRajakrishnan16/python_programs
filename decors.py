def make_title(original_func):
    def wrapper_func(*name):
        str = original_func(*name)
        return str.title()
    return wrapper_func

def replace_alice(func):
    def wrap_rep(*name):
        str = func(*name)
        return str.replace('alice', 'apple')
    return wrap_rep

#Inner decor is first called. So replace_alice first replaces alice with apple and then send for title casing decor. If make_title was the inner most decor, that would have got called and alice would have become Alice and there would be no alice for replace_alice decor to replace.
@make_title
@replace_alice
def greet(name):
    return f'hello, {name}'

@make_title
def greet_two(*name):
    return f'hello, {name[0]} {name[1]}'

print(greet('alice'))
print(greet_two('alice','bob'))