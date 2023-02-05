# 산봉우리 = 같은 높이를 가지는 하나의 격자 or 인접한 격자들의 집합.
# 인접 == X좌표와 Y좌표 차이가 모두 1이하
# 산봉우리인접격자 < 산봉우리
# 산봉우리 몇개?

import sys
read = sys.stdin.readline

n, m = map(int, input().split()) # N x M 격자 100X70
A = [list(map(int, read().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]


def dfs(r, c):
    global top
    visited[r][c] = 1
    dr = [1, 1, 1, -1, -1, -1, 0, 0]
    dc = [0, -1, 1, 0, -1, 1, -1, 1]
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<= nr < n and 0 <= nc < m:
            if A[nr][nc] > A[r][c]: #탐색칸이 나보다 높음
                top = False
            if visited[nr][nc] == 0 and A[nr][nc] == A[r][c]: #같은높이
                dfs(nr, nc)
    
cnt = 0
for r in range(n):
    for c in range(m):
        if A[r][c] > 0 and visited[r][c] == 0:
            top = True 
            dfs(r, c)
            if top:                                                                                                   
                cnt += 1

print(cnt)                                                                  