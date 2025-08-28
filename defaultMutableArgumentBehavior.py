def foo(a, b=[]):
    b.append(a)
    return b


result1 = foo(1)
result2 = foo(2, [])
result3 = foo(3)

print(result1)
print(result2)
print(result3)
