H, M = map(int,input().split())
i = 45-M
if M < 45:    
    M = 60-i
    H = H-1
    if H < 0:
        H = 23
else:
    M = M-45
print(H, M)