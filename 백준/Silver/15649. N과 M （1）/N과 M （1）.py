import itertools

n, m = map(int,input().split())

_list = []
for i in range(1,n+1):
    _list.append(i)

iter = itertools.permutations(_list, m)

for j in iter:
    print(' '.join(map(str, j)))