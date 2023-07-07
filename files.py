path = 'test.txt'
f = open(path)
print(f.tell())
lines = [x.rstrip() for x in f]
print(f.tell())
print(lines)
f.close()
print(f.closed)

# This will automatically close the file f when exiting the with block
with open(path) as f:
    lines = [x.rstrip() for x in f]
    print(lines)


