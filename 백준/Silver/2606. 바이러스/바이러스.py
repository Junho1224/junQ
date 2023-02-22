#바이러스

com = int(input())
net = int(input())

graph = [[] for _ in range(com+1)] # 컴퓨터 번호를 인덱스로 하는 그래프
visited = [0]*(com+1) # 방문 체크

# 그래프 입력
for _ in range(net):
    a, b = map(int, input().split())
    graph[a].append(b) # graph[a] += [b]
    graph[b].append(a)

# DFS
def dfs(com):
    visited[com] = 1
    for i in graph[com]:
        if not visited[i]:
            dfs(i)
dfs(1)
print(sum(visited) - 1)


# BFS
# def bfs(com):
#     from collections import deque
#     q = deque([com])
#     visited[com] = 1
#     while q:
#         v = q.popleft()
#         for i in graph[v]:
#             if not visited[i]:
#                 q.append(i)
#                 visited[i] = 1
# bfs(1)
# print(sum(visited) - 1)