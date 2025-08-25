from datetime import date
s = 'Hello, world.'
print(str(s))
print(repr(s))
print(str(1/7))
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(str('hello, world\n'))
print(hellos)
# The argument to repr() may be any Python object:
repr((x, y, ('spam', 'eggs')))
d =date(2025, 8, 25)
print(str(d))
print(repr(d))