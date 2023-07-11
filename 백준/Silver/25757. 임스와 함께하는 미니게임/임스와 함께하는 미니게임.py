import sys

input = sys.stdin.readline

a, b = input().split()
name = []
minigame = {"Y": 1, "F": 2, "O": 3}
a = int(a)
for i in range(a):
    c = input()
    name.append(c)
name1 = set(name)

result = len(name1)
print(result//minigame[b])