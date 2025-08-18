# list_ops_demo_strings.py
# A small showcase of Python list operations using strings.

b = ['apple', 'banana', 'cherry', 'banana']

# Add items to the end (single and multiple)
b.append('date')
b[len(b):] = ['elderberry']  # same as extend(['elderberry'])
print(b)

# Extend with multiple items
b.extend(['fig', 'grape'])
print(b)

# Another extend via slice assignment
b[len(b):] = ['honeydew', 'kiwi']
print(b)

# Insert at a specific position
b.insert(1, 'blueberry')
print(b)

# Remove first occurrence by value
b.remove('banana')
print(b)

# Pop the last item and a specific index
item = b.pop()
print(item)
item2 = b.pop(3)
print(item2)

# Inspect: index, length, counts
print(b)
print(b.index('grape'))  # find the position of 'grape'
print(len(b))  # list length
print(b.count('banana'))  # 'banana' count after one remove
print(b.count('fig'))  # count of 'fig'

# Reverse and sort (ascending and descending)
b.reverse()
print(b)

b.sort()
print(b)

b.sort(reverse=True)
print(b)
