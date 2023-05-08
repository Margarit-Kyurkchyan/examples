import re

states = ['  Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda', 'south    carolina##', 'West virginia?']


def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?]', '', value)
        value = value.title()
        result.append(value)
    return result


print(clean_strings(states))


# an alternative approach

def remove_punctuation(value):
    return re.sub('[!#?]', '', value)


clean_ops = [str.strip, remove_punctuation, str.title]


def clean_strings_v2(strings, ops):
    result = []
    for value in strings:
        for func in ops:
            value = func(value)
        result.append(value)
    return result


print(clean_strings_v2(states, clean_ops))

for x in map(remove_punctuation, states):
    print(x)
