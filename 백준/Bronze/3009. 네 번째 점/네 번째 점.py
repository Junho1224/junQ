x = []
y = []
a = 0
b = 0
for i in range(3):
   a, b = map(int,input().split())
   x.append(a)
   y.append(b)

if x[0] == x[1]:
   a = x[2]
if x[0] == x[2]:
   a = x[1]
if x[1] == x[2]:
   a = x[0]

if y[0] == y[1]:
   b = y[2]
if y[0] == y[2]:
   b = y[1]
if y[1] == y[2]:
   b = y[0]

print(a, b)