# Namespaces, Scope, and Local Functions
a = []


def func():
    for i in range(5):
        a.append(i)


func()
print(a)

b = None


def bind_b_variable():
    b = []


bind_b_variable()
print(b)

# using the global
c = None


def bind_c_variable():
    global c
    c = []


bind_c_variable()
print(c)


# Returning Multiple Values
def f():
    a = 5
    b = 6
    c = 7
    return a, b, c


d, e, g = f()
print(e)
h = f()
print(h)
