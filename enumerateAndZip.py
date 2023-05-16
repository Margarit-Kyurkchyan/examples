# enumerate function
some_list = ['foo', 'bar', 'baz']
mapping = {}
for i, v in enumerate(some_list):
    mapping[v] = i
print(mapping)

# sorted function
print(sorted([7, 1, 2, 6, 0, 3, 2]))
print(sorted("the man who sold the world"))

# zip
seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three']
zipped = zip(seq1, seq2)
print(zipped)
print(list(zipped))

for i, (a, b) in enumerate(zip(seq1, seq2)):
    print('{0}: {1}, {2}'.format(i, a, b))

pitchers = [('Nolan', 'Ryan', 4), ('Roger', 'Clemens', 25), ('Curt', 'Schilling', 39)]
first_names, last_names, age = zip(*pitchers)
print('{0}, {1}, age {2}'.format(first_names, last_names, age))

# reversed
print(list(reversed(range(10))))
