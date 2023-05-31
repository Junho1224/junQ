#3046 R2
# S = (R1+R2)/2

R1, S = map(int, input().split())
R2 = (S - R1/2) * 2
print(int(R2))