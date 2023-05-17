from functools import partial


def add_numbers(x, y):
    return x + y


add_five = lambda y: add_numbers(5, y)
print(add_five(99))

# The built-in functools module can simplify this process using the partial function
add_five2 = partial(add_numbers, 5)
print(add_five2(100))
