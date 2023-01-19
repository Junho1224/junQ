n = int(input()) #26
num = n # 
count = 0

while True:
    a = num//10 #2 6 8 4
    b = num%10 #6 8 4 2
    c = (a+b)%10 # 8 14 12 6
    num = (b*10)+c #68 84 42 26
    
    count += 1
    if num == n:
        break

print(count)