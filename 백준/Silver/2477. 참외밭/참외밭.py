import sys
input = sys.stdin.readline
garo = []
sero = []
m1 = []
m2 = []

n = int(input())

for i in range(6):
    a, b = map(int, input().split())
    if a == 1 or a == 2:
        garo.append(b)
    else:
        sero.append(b)
    m1.append(a)
    m2.append(b)
bigbox = max(garo) * max(sero)

for j in range(3):
    if m1[j] == m1[j+2] and m1[j+1] == m1[j+3]:
        smallbox = m2[j+1] * m2[j+2]
    elif m1[0] == m1[2] and m1[1] == m1[5]:
        smallbox = m2[0] * m2[1]
    elif m1[0] == m1[4] and m1[1] == m1[5]:
        smallbox = m2[0] * m2[5]
    elif m1[0] == m1[4] and m1[3] == m1[5]:
        smallbox = m2[4] * m2[5]
box = bigbox - smallbox
print(box*n)