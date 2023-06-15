# 14659 한조어쩌구 ㅋㅋ

n = int(input())
bong = list(map(int, input().split()))
ans = 0
maxbong = 0
count = 0

for i in bong:
    if i > maxbong:
        maxbong = i
        count = 0
    else:
        count += 1
    # print(count)
    ans = max(ans,count)
    
print(ans)    