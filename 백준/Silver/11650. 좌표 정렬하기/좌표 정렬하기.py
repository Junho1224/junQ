n = int(input())

_list = []

for i in range(n):
    a = list(map(int,input().split()))
    _list.append(a)

_list.sort(key=lambda item: (item[0], item[1])) 

for i in _list:
    print(*i)
