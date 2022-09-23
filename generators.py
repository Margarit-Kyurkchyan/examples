import itertools

# group by
first_letter = lambda x: x[0]
names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']
for letter, names in itertools.groupby(names, first_letter):
    print(letter, list(names))

# combinations
fruits = ['orange', 'apple', 'mango', 'fig']
print('\ncombinations')
for c in itertools.combinations(fruits, 2):
    print(c)

# permutations
print('\npermutations')
for c in itertools.permutations(fruits, 2):
    print(c)

# product
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
print('\nproduct')
for p in itertools.product(arr1, arr2):
    print(p)