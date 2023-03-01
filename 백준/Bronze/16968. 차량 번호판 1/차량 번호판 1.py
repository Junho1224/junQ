n = list(input())

ans = 1

if n[0] =='c':
    ans = 26
else:
    ans = 10

for i in range(1, len(n)):
    if n[i] == 'c':
        if n[i-1] == 'c':
            ans *= 25
        else:
            ans *= 26

    else:
        if n[i-1] == 'd':
            ans *= 9
        else:
            ans *= 10
print(ans)