from collections import deque

# twelve = '0123456789AB'
pipe = { # 0, 1, 2, 3
	'0': [0, 0, 0, 0], #0
	'1': [0, 1, 0, 1], #1
	'2': [1, 0, 1, 0], #2
	'3': [0, 1, 1, 0], #3
	'4': [0, 0, 1, 1], #4
	'5': [1, 0, 0, 1], #5
	'6': [1, 1, 0, 0], #6
	'7': [1, 1, 1, 0], #7
	'8': [0, 1, 1, 1], #8
	'9': [1, 0, 1, 1], #9
	'A': [1, 1, 0, 1], #A
	'B': [1, 1, 1, 1]  #B
}

N = int(input())
x, y = map(int, input().split()) # x가로 y 세로
A = []
visited = [[0 for _ in range(N)] for _ in range(N)]
zero = 0

for i in range(N):
	A.append(list(input()))
	for j in range(N):
		if A[i][j] == '0':
			zero += 1

pipe_cnt = N*N-zero
water = 0

q = deque()
q.append([y, x])
visited[y][x] = 1
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1] # 0 1 2 3

while q:
	r, c = q.popleft()
	# print(r,c)
	water += 1
	for i in range(4):
		if pipe[A[r][c]][i]:
			nr = r + dr[i]
			nc = c + dc[i]
			if 0 > nr or N <= nr or 0 > nc or N <= nc or A[nr][nc] == '0':
				continue
			if visited[nr][nc] == 0:
				if pipe[A[nr][nc]][(i+6)%4]:
					visited[nr][nc] = 1
					q.append([nr,nc])

# print(pipe_cnt, water)
print(pipe_cnt - water)
				
				