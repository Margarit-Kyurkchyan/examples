def apply_to_list(some_list, f):
    return [f(x) for x in some_list]


ints = [4, 0, 1, 5, 6]
print(apply_to_list(ints, lambda x: x * 2))

# to sort a collection of strings by the number of distinct letters in each string
strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
strings.sort(key=lambda x: len(set(list(x))))
print(strings)