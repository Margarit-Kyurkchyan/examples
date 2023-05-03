# given a list of strings, filter out strings with length 2 or less and also convert them to uppercase
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
upper_strings = [x.upper() for x in strings if len(x) > 2]
print(upper_strings)

# get a set containing just the lengths of the strings contained in the collection
unique_lengths = {len(x) for x in strings}
print(unique_lengths)

# map function
unique_lengths = set(map(len, strings))
print(unique_lengths)

# a lookup map of the strings to their locations in the list
loc_mapping = {val: index for index, val in enumerate(strings)}
print(loc_mapping)

# nested list comprehensions
# to get a single list containing all names with two or more a’s in them.
all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'], ['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]
names_of_interest = []
for names in all_data:
    enough_as = [name for name in names if name.count('a') >= 2]
    names_of_interest.extend(enough_as)
print(names_of_interest)

# use a single nested list comprehension
result = [name for names in all_data for name in names if name.count('a') >= 2]
print(result)
