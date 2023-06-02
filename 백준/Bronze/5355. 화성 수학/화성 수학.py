# 화성 수학
for i in range(int(input())):
    a = list(map(str, input().split()))
    b = 0

    for j in range(1,len(a)):
        if b == 0:
            b = float(a[0])
        if a[j] == "@":
            b*=3
        elif a[j] == "%":
            b+=5
        else:
            b-=7
    print("%.2f" %b)