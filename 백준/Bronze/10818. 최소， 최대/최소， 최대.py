# 10818
b = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
print(a[-1], a[0])