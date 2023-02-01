# 국영수
#국어 점수가 감소
#영어 점수가 증가
#수학 점수가 감소
#이름이 증가
import sys
input = sys.stdin.readline

n = int(input())
data=[]

for i in range(n):
    a = list(input().split())
    data.append((a[0],int(a[1]),int(a[2]),int(a[3])))

    # a = input().split()
    # for i in range(3):
    #     a[i+1] = int(a[i+1])
    # data.append(a)
data.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(data[i][0])