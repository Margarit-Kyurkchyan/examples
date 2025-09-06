arg = 'workfile.txt'
try:
    f = open(arg, 'r')
except OSError:
    print('cannot open', arg)
else:
    print(arg, 'has', len(f.readlines()), 'lines')
    f.close()
