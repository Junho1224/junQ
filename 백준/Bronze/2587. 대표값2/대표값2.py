f = []

for i in range(5):
    f.append(int(input()))


ave = int(sum(f) / 5)
print(ave)
f.sort()
print(f[2])