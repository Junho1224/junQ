import sys
input =  sys.stdin.readline

n = int(input())

_list = []

for i in range(n):
    a = list(map(int,input().split()))
    _list.append(a)

_list.sort(key=lambda item: (item[1], item[0])) 

for i in _list:
    print(*i)

