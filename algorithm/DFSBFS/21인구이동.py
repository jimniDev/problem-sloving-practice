#21인구이동.py
#dfs bfs 둘다 되어ㅓ보일때는 bfs쓰기

from collections import deque

N, L, R = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))
#print(A)

dx = [-1,1,0,0] 
dy = [0,0,-1,1] 

def bfs(x, y, index):
    q = deque()
    q.append((x,y))

    sum_ = A[x][y]
    count = 1 
    union = []
    union.append((x,y))

    visited[x][y] = index # 연합번호

    while q:
        q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == -1 and L <= abs(A[x][y] - A[nx][ny]) <= R:
                    q.append((nx, ny))
                    visited[nx][ny] = index 
                    sum_ += A[nx][ny]
                    count += 1
                    union.append((nx,ny))
    for i, j in union:
        A[i][j] = sum_ // count
    return count

#인구이동
move_cnt = 0 # 이동 횟수
while True:
    visited = [[-1] * N for _ in range(N)]
    index = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1:
                bfs(i, j, index)
                index += 1
                print(A)
    if index == N*N:
            break
    move_cnt += 1
        


print(move_cnt)

