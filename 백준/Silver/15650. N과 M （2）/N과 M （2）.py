import itertools

n, m = map(int,input().split())

_list = []
for i in range(1,n+1):
    _list.append(i)

iter = itertools.combinations(_list, m)

for j in iter:
    print(*j)