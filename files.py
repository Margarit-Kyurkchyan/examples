path = 'test.txt'
f = open(path)
print(f.tell())
lines = [x.rstrip() for x in f]
print(f.tell())
print(lines)
print(f.read())
f.close()
print(f.closed)

# This will automatically close the file f when exiting the with block
with open(path) as f:
    lines = [x.rstrip() for x in f]
    print(lines)

f = open('workfile.txt', 'w', encoding="utf-8")
f.write('What is Lorem Ipsum? \nWhere does it come from?')

print(f.closed)
f.close()
print(f.closed)

with open('workfile.txt', encoding="utf-8") as f:
    read_data = f.read()

print(f.closed)
