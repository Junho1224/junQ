N = int(input())
ct = 0
ans = 0
num = 666

while True:

    if '666' in str(num):
        ct += 1

    if ct == N:
        ans = num
        break

    num += 1

print(ans)