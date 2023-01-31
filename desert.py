# from collections import deque
#
# N = int(input())
# M = [list(map(int, input().split())) for _ in range(N)]
#
# dx = [-1, -1, 1, 1]
# dy = [-1, 1, -1, 1]
#
# def bfs(i_x, i_y):
#     visited = [[0] * N for _ in range(N)]
#     desert = []
#     q = deque()
#     q.append([i_x,i_y, 0, -1])
#     desert.append(M[i_x][i_y])
#     while q:
#         x, y, cnt, dir = q.popleft()
#         if x == i_x and y == i_y and cnt == 4: #종료조건
#             print('종료', len(desert))
#             return len(desert)
#         elif cnt == 0: # 시작은 오른쪽 아래로
#             nx = x + dx[3]
#             ny = y + dy[3]
#             if 0 <= nx < N and 0 <= ny < N and M[nx][ny] != M[i_x][i_y]:
#                 q.append([nx, ny, 1, 3])
#                 desert.append(M[nx][ny])
#         elif cnt < 5:
#             for d in range(4):
#                 nx = x+dx[d]
#                 ny = y+dy[d]
#                 if 0<=nx<N and 0<=ny<N:
#                     if nx == i_x and ny == i_y and cnt > 1:
#                         if d == dir:
#                             q.append([nx, ny, cnt, d])
#                         else:
#                             q.append([nx, ny, cnt+1, d])
#                     elif M[nx][ny] not in desert:
#                         if d == dir:
#                             q.append([nx, ny, cnt, d])
#                             desert.append(M[nx][ny])
#                         else:
#                             q.append([nx, ny, cnt + 1, d])
#                             desert.append(M[nx][ny])
#         print(desert, cnt)
#
#
# for r in range(N):
#     for c in range(N):
#         cur = bfs(r,c)
#         print(r,c, cur)
#         max = cur if max < cur else max
#
#
# print(max)
from collections import deque

T = int(input())
dx = [-1, -1, 1, 1]
dy = [-1, 1, -1, 1]

for test_case in range(1, T + 1):
    max = -1
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    for i_x in range(N):
        for i_y in range(N):
            desert = []
            q = deque()
            q.append([i_x,i_y, 0, -1])
            desert.append(M[i_x][i_y])
            while q:
                x, y, cnt, dir = q.popleft()
                if x == i_x and y == i_y and cnt == 4: #종료조건
                    max = len(desert) if max < len(desert) else max
                elif cnt == 0: # 시작은 오른쪽 아래로
                    nx = x + dx[3]
                    ny = y + dy[3]
                    if 0 <= nx < N and 0 <= ny < N and M[nx][ny] != M[i_x][i_y]:
                        q.append([nx, ny, 1, 3])
                        desert.append(M[nx][ny])
                elif cnt < 5:
                    for d in range(4):
                        nx = x+dx[d]
                        ny = y+dy[d]
                        if 0<=nx<N and 0<=ny<N:
                            if nx == i_x and ny == i_y and cnt > 1:
                                if d == dir:
                                    q.append([nx, ny, cnt, d])
                                else:
                                    q.append([nx, ny, cnt+1, d])
                            elif M[nx][ny] not in desert:
                                if d == dir:
                                    q.append([nx, ny, cnt, d])
                                    desert.append(M[nx][ny])
                                else:
                                    q.append([nx, ny, cnt + 1, d])
                                    desert.append(M[nx][ny])
                print(desert, cnt)

    print('#{} {}'.format(test_case,max))
