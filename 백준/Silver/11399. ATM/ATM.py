# 11399 알레띠
n =  int(input())
abc = list(map(int, input().split()))

abc.sort()
anw = 0

for i in range(1, n+1):
    anw += sum(abc[0:i])
print(anw)
    