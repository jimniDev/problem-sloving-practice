# 토지 구입비용 최소
# 0,0과 n-1,n-1 연결
# 0이면 이미 회사소유
# 1:10 ~

from collections import deque

n = int(input())
A = [list(map(int, input())) for _ in range(n)]
q = deque()
q.append((0,0))
visited = [[1e9 for _ in range(n)] for _ in range(n)]
visited[0][0] = 0

dr, dc = [1,-1,0,0], [0,0,-1,1]

while q:
	r, c = q.popleft()
	for i in range(4):
		nr = r + dr[i]
		nc = c + dc[i]
		if 0 <= nr < n and 0 <= nc < n:
			if visited[nr][nc] == 1e9 or (visited[nr][nc] != 1e9 and A[nr][nc] + visited[r][c] < visited[nr][nc]):
				visited[nr][nc] = min(A[nr][nc] + visited[r][c], visited[nr][nc])	
				q.append((nr, nc))
				
print(visited[n-1][n-1])