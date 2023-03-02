# 윷놀이


for _ in range(3):
    a, b, c, d = map(int, input().split())
    s = sum([a, b, c, d])
    
    if s == 4:
        print("E")
    elif s == 3:
        print("A")
    elif s == 2:
        print("B")
    elif s == 1:
        print("C")
    else:
        print("D")