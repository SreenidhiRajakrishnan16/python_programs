import sys

# 🌍 GLOBAL NAMESPACE
x = 'global_x'
y = 'global_y'


def outer():
    # 🧱 ENCLOSING (OUTER FUNCTION) NAMESPACE
    print('\n[x from global]:', x)
    # Output → x from global: global_x

    # This 'y' shadows the global y — now local to outer()
    y = 'enclosing_y'

    def inner():
        # 💡 LOCAL (INNER FUNCTION) NAMESPACE
        # Accessing 'y' from the enclosing scope (outer)
        print('\n[y from outer enclosing]:', y)
        # Output → y from outer enclosing: enclosing_y

        # locals() inside inner() → shows inner’s own local namespace
        print('\n[Local workspace of inner function]:', locals())
        # Output → {'y': 'enclosing_y'}

    # Call inner() — closure is formed & used immediately
    inner()

    # Access closure from the inner function object
    print('\n[Accessing closure created in inner() from outer()]:',
          inner.__closure__[0].cell_contents)
    # Output → Accessing closure created in inner() from outer(): enclosing_y

    # locals() in outer() shows outer’s namespace (y + inner function)
    print('\n[Local workspace of enclosing outer() function]:', locals())
    # Output → {'y': 'enclosing_y', 'inner': <function outer.<locals>.inner at 0x...>}


# 🔹 Execute outer() — creates enclosing and local scopes
outer()

# 🌍 GLOBAL SCOPE
print('\n[Locals from global location]:', locals())
# Output → {'sys': <module 'sys' (built-in)>, 'x': 'global_x', 'y': 'global_y', 'outer': <function outer at 0x...>}

print('\n[Globals() namespace]:', globals())
# Output → (same as above, module-level namespace)

print('\n[Dict of current module via sys.modules]:',
      sys.modules[__name__].__dict__)
# Output → (same dictionary as globals())

print('\n(locals() is globals() is sys.modules[__name__].__dict__):',
      locals() is globals() is sys.modules[__name__].__dict__)
# Output → True
