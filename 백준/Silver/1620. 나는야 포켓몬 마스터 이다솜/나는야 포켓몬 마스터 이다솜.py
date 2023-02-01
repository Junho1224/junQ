# 나는야 포켓몬 마스터 이다솜

import sys
input = sys.stdin.readline

dic={}

a,b=map(int,input().split())

for i in range(a):
    p=input().strip()

    dic[p]=str(i+1)
    dic[str(i+1)]=p
for i in range(b):
    q = input().strip()
    print(dic[q])