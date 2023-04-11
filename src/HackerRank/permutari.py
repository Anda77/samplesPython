from itertools import permutations

s,n = input().split()
print(s)
print(n)
n = int(n)
pmtn = sorted(permutations(s,n))

for i in pmtn:
    print(''.join(i))