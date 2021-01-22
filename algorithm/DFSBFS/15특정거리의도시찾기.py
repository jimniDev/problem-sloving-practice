# 아이디어1. 최단거리보고 bfs로 접근

# from collections import deque

# N, M, K, X = map(int, input().split())
# print(N, M, K, X)
# graph = [[] for i in range(N+1)]
# # 와 graph [[]]*N의 차이는 뭐야?
# dis = []
# visited = [False]*(N+1)

# for i in range(M):
#     start, end = map(int, input().split())
#     graph[start].append(end)

# def bfs(graph, start, dis):
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         queue.popleft()
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i]=True
#                 dis[i] = dis[i]+1
# print(graph)

from collections import deque

N, M, K, X = map(int, input().split())
graph = [[] for i in range(N+1)]
dis = [-1]*(N+1)
dis[X] = 0 # 이걸안해줫음 

for i in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)

queue = deque([X])
while queue:
    now = queue.popleft()
    for next_city in graph[now]:
        if dis[next_city] == -1:
            queue.append(next_city)
            dis[next_city] = dis[now]+1

check = False
for i in range(1, N+1):
    if dis[i] == K:
        print(i)
        check = True
if check == False:
    print(-1)

#시간초과남
 