# 직사각형 네개의 합집합 면적 구하기

import sys
input = sys.stdin.readline

qwer = [[0] * 100 for i in range(100)]
q = 0

for j in range(4):
    a, b, c, d = map(int, input().split())
    for i in range(a, c):
        for j in range(b, d):
            if qwer[i][j] == 0:
                qwer[i][j] += 1
                q += 1
print(q)
