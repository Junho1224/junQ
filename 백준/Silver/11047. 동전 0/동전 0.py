# 동전 0
a, b = map(int, input().split())
coin = []
count = 0

for i in range(a):
    c = int(input())
    coin.append(c)
coin.sort(reverse=True)

for i in coin:
    count += b // i
    b %= i
print(count)
    
