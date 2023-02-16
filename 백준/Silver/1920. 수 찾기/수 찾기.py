import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(map(int, input().split()))

m = int(input())
target = list(map(int, input().split()))



def binary_search(arr, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if arr[mid] == target:
        return 1
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)

for i in range(m):
    print(binary_search(arr, target[i], 0, len(arr)-1))