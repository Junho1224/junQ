n = int(input())

def factorial(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans

ans = 0

num = str(factorial(n))[::-1]
for i in num:
    if i != '0': # 문자
        break
    ans += 1


print(ans)