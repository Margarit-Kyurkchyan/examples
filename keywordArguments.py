def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    print(arguments)
    for arg in arguments:
        print(arg)
    print(keywords)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           kfff="ddd",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


def display_info(first, second, *extras, category, detail, **options):
    print("First argument:", first)
    print("Second argument:", second)
    print("Extra positional args:", extras)
    print("Keyword options:", options)


# Example usage
display_info(
    10,
    20,
    30, 40, 50,
    category="Books",
    detail="Fiction",
    author="Orwell",
    year=1949
)


# Special parameters
def standard_arg(arg):
    print(arg)


def pos_only_arg(arg, /):
    print(arg)


def kwd_only_arg(*, arg):
    print(arg)


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


standard_arg(2)
standard_arg(arg=2)

pos_only_arg(1)
# pos_only_arg(arg=1)

combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)


# combined_example(1, 2, 3)
# combined_example(pos_only=1, standard=2, kwd_only=3)

def foo(name, **kwargs):
    return 'name' in kwargs


# foo(1, **{'name': 2})

def foo(name, /, **kwargs):
    return 'name' in kwargs


print(foo(1, **{'name': 2}))


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(22)
print(f(0))
print(f(1))


def make_incrementor(n):
    """Lambda-free equivalent using a nested function that closes over n."""

    def increment(x):
        return x + n

    return increment


f2 = make_incrementor(11)
print(f2(20))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)


def sort_pairs_def(pairs: list[tuple[int, str]]) -> list[tuple[int, str]]:
    """Use a named function as the key (no lambda)."""

    def second(pair: tuple[int, str]) -> str:
        return pair[1]

    return sorted(pairs, key=second)


def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass


print(my_function.__doc__)

def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and' + eggs

f('spam')