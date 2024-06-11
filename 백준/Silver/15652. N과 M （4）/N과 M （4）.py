import sys

input = sys.stdin.readline

n, m = map(int,input().split()) 

array = []

def dfs(start):
    if len(array) == m: 
        for i in array:
            print(i, end = ' ')
        print()
        return 
    
    for i in range(start, n + 1):
        array.append(i)
        dfs(i)
        array.pop()

dfs(1)