n = int(input())

for i in range(n):
    name = ''
    max = 0
    m = int(input())
    for i in range(m):
        a, b = input().split()
        b = int(b)
        if max < b:
            max = b
            name = a
    print(name)