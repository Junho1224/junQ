# 거스름돈
n = int(input())
count = 0
change = 1000 - n

while True:
    if change >= 500:
        while change > 499:
            change = change - 500
            count += 1
        
    if change >= 100:
        while change > 99:
            change = change - 100
            count += 1
        
    if change >= 50:
        while change > 49:
            change = change - 50
            count += 1
        
    if change >= 10:
        while change > 9:
            change = change - 10
            count += 1

    if change >= 5:
        while change > 4:
            change = change - 5
            count += 1

    if change >= 1:
        while True:
            change = change - 1
            count += 1
            if change == 0:
                break
            
            
    break
print(count)
