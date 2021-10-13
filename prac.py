from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(x,y):
    q = deque()
    q.append((x,y))

    while queue:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #벗어난경우
            if nx<0 or nx >= n or ny<0 or ny>=m:
                continue
            #벽인경우
            if graph[nx][ny] == 0:
                continue
            #처음 방문인 경우 최단거리 기록
            if graph[nx][ny] == 1:
                grapah[nx][ny] = graph[nx][ny] + 1
        return graph[n-1][m-1]

    print(BFS(0,0))


def spread_virus(r,c, sel_NM):
    if sel_NM[r][c] == 2:
        for dir in range(4):
            n_r = r+dr[dir]
            n_c = c+dc[dir]
            if n_r >= 0 and n_c >= 0 and n_r<N and n_c < M:
                if sel_NM[n_r][n_c] == 0:
                    sel_NM[n_r][n_c] =2
                    spread_virus(n_r, n_c, sel_NM)

list.sort()
sdic = sorted(dict.items(), reverse=True)
sorted(str_list, key=lambda x: x[1])
tuple_list.sort(key=lambda x: (x[0], x[1]))

from collections import Counter

import bisect

from queue import PriorityQueue
que = PriorityQueue()
que.put(4)
print(que.get())