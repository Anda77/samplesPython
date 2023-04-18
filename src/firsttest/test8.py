dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)

print(dct)

print(dct.keys())

for x in dct.keys():
    print(dct[x][1], end='')
