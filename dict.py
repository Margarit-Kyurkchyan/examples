from collections import defaultdict

# Categorizing a list of words by their first letters as a dict of lists
words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}
for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)
print(by_letter)

# The setdefault dict method can be used to simplify this workflow.
by_letter2 = {}
for word in words:
    letter = word[0]
    by_letter2.setdefault(letter, []).append(word)
print(by_letter2)

# The built-in collections module has a useful class, defaultdict, which makes this even easier.
by_letter3 = defaultdict(list)
for word in words:
    by_letter3[word[0]].append(word)
print(by_letter3)