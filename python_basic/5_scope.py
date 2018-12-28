# import builtins

# print(dir(builtins))

x = 'global_x'


def test():
    # global x         # do change the x
    x = 'local_x'  # do not change the x (global_x)
    print(x)


test()
print(x)


def outer():
    x = 'outer_x'

    def inner():
        nonlocal x
        x = 'inner_x'
        print(x)
    inner()
    print(x)


outer()
