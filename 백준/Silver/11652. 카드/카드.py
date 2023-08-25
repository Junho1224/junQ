from collections import Counter
import sys

input = sys.stdin.readline

n = int(input())

_list = []

for i in range(n):
    a = int(input())
    _list.append(a)

a_ = Counter(_list)
sorted_a = sorted(a_.items(), key=lambda x: (x[1], -x[0]), reverse=True)

a_max = sorted_a[0][0]
# a_max = max(a_, key = a_.get)

print(a_max)
