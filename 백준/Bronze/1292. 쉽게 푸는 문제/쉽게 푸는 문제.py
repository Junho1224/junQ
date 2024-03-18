a,b = map(int,input().split())

arr = [0]
for i in range(46):
    for j in range(i):
        arr.append(i)
suma = sum(arr[a:b+1])
print(suma)
