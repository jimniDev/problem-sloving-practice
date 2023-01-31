import sys
import copy
from collections import deque

input = sys.stdin.readline
p = int(input())
cnt = 0
ans = 0

dx = [0,0,0, 1,-1]
dy = [0,1,-1, 0,0]

def filp(grid, x, y):
    tmp = copy.deepcopy(grid)
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 3 and 0 <= ny < 3:
            tmp[nx][ny] = 1 if grid[nx][ny] == 0 else 0
    return tmp

def grid_binary(grid):
    binary = ''
    for i in range(3):
        for j in range(3):
            binary += str(grid[i][j])
    return int(binary, 2)

def match(a, b):
    for i in range(3):
        for j in range(3):
            if a[i][j] != b[i][j]:
                return False
    return True

def bfs(sample):
    cnt = 0
    all_white = [[0]*3 for _ in range(3)]
    visited = [0]*10000

    q = deque([all_white])
    visited[grid_binary(all_white)] = 1
    while q:
        for _ in range(len(q)):
            grid = q.popleft()
            if match(grid, sample):
                return cnt
            for i in range(3):
                for j in range(3):
                    next_grid = filp(grid, i, j)
                    binary = grid_binary(next_grid)
                    if not visited[binary]:
                        q.append(next_grid)
                        visited[binary] = 1
        cnt += 1

for _ in range(p):
    sample = []
    for _ in range(3):
        arr = list(str(input().rstrip()))
        sample.append([1 if x == '*' else 0 for x in arr])
    print(bfs(sample))


#00 01 11
#10 11 12
#20 21 22


