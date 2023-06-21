gen = (x ** 2 for x in range(100))
print(gen)

# Generator expressions can be used instead of list comprehensions as function arguments in some cases:
print(sum(x ** 2 for x in range(100)))
print(dict((i, i ** 2) for i in range(5)))