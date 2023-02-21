from itertools import combinations
from collections import deque
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6) #50x50 테케 시 

n, m = map(int, input().split())
A = [list(map(int, read().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
dr, dc = [1,-1,0,0], [0,0,1,-1]
closes = []

def find_land(r, c, num):
    global n,m,A,visited
    close = []
    visited[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr <n and 0 <= nc <m:
            if A[nr][nc] == 0 and (r,c) not in close:
                visited[nr][nc] = 1
                close.append((r,c))
            if A[nr][nc] == 1 and visited[nr][nc] == 0:
                A[nr][nc] = num
                visited[nr][nc] = 1
                close += find_land(nr,nc,num)
    return close
	
num = -1
for r in range(n):
    for c in range(m):
        if A[r][c] == 1 and visited[r][c] == 0:
            closes.append(find_land(r,c, num)) # 섬 개수만큼 close 배열들 생김
            num -= 1
						
land_cnt = len(closes)
min_dis = 1e9
# print(closes)
# print(A)

for a in closes[0]:
	for b in closes[1]:
		dis = abs(a[0]-b[0]) + abs(a[1]-b[1]) -1
		min_dis = min(min_dis, dis)

print(min_dis)