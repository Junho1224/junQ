change = [25,10,5,1]
count = [0]*4
for i in range(int(input())):
    C = int(input())

    for j in range(len(change)):
        count[j] = C // change[j]
        C = C % change[j]

    print(" ".join(map(str,count)))