#17144미세먼지.py
from collections import deque
import copy

R,C,T = map(int, input().split())
m = []
for _ in range(R):
    m.append(list(map(int, input().split())))

cleaner = -1
for i in range(R):
    for j in range(C):
        if m[i][j] == -1:
            cleaner = i #아랫칸 행 저장

def spread_dust():
    dust = deque()
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for i in range(R):
        for j in range(C):
            if m[i][j] > 0:
                dust.append((i,j, m[i][j]))

    for _ in range(len(dust)):
        x, y, A = dust.popleft()
        dir_cnt = 0 
        for i in range(4):
            r = x + dx[i]
            c = y + dy[i]
            if 0 <= r < R and 0 <= c < C and m[r][c] != -1:
                dust.append((r,c, m[x][y]//5))
                dir_cnt +=1
        m[x][y] -= m[x][y]//5*dir_cnt
    while dust:
        x, y, A = dust.popleft()
        m[x][y] += A

def clean_dust(m, cleaner):
    up = cleaner-1
    down = cleaner

    for i in range(up-1, 0, -1):
        m[i][0] = m[i-1][0]
    for j in range(1,C):
        m[0][j-1] = m[0][j]
    for i in range(up):
        m[i][C-1] = m[i+1][C-1]
    for j in range(C-1, 1, -1):
        m[up][j] = m[up][j-1]
    m[up][1] = 0
    
    for i in range(down+2 ,R):
        m[i-1][0] = m[i][0]
    for j in range(1,C):
        m[R-1][j-1] = m[R-1][j]
    for i in range(R-1, down, -1):
        m[i][C-1] = m[i-1][C-1]
    for j in range(C-1, 1, -1):
        m[down][j] = m[down][j-1]
    m[down][1] = 0
    return m 

for i in range(T):
    spread_dust()
    m = clean_dust(m, cleaner)

total = 0
for i in range(R):
    for j in range(C):
        if m[i][j] > 0:
            total += m[i][j]
print(total)



    