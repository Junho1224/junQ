n = int(input())
m = list(map(int, input().split()))

mm = list(set(m))
print(len(m)-len(mm))