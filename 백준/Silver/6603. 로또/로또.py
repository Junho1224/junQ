import sys
from itertools import combinations

input = sys.stdin.readline

while True:
    
    s = list(map(int, input().split()))[1:]
    # print(s)
    if s == []:
        break

    for i in combinations(s, 6):
        print(*i)
    print('')