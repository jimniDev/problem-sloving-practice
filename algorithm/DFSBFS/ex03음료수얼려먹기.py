n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

print(graph)

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 0: # 방문안했다면
        graph[x][y] = 1  #방문
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

result = 0 
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result += 1

print(result)

