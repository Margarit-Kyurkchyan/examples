import json

f = open('jsonDump.txt', 'w')
x = [1, 'simple', 'list']
json.dumps(x)
json.dump(x, f)
f.close()
f = open('jsonDump.txt', 'r')
x = json.load(f)
print(x)
