import sys
import copy
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)


N, Q = map(int, input().split())
board_size = 2**N
board = [list(map(int, input().split())) for _ in range(board_size)]
stages = list(map(int, input().split()))
print(stages)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def firestorm(stage, board):
    stage_size = 2**stage
    A = copy.deepcopy(board)
    for r_idx, rr in enumerate(range(0, board_size, stage_size)):
        cc_start = 0 if r_idx % 2 == 0 else stage_size
        for cc in range(cc_start, board_size, stage_size*2):
            #print(stage, rr, cc)
            #격자돌리기
            for r in range(0,stage_size):
                for c in range(0, stage_size):
                    A[rr + c][cc + stage_size-1-r] = board[rr+r][cc+c]
                    #print(rr + c, cc + stage_size-1-r, '|', rr+r, cc+c)

    melt_ice = []
    for r in range(0, board_size):
        for c in range(0, board_size):
            safe = 0
            if A[r][c] > 0:
                for i in range(4):
                    x = r+dx[i]
                    y = c+dy[i]
                    if 0 <= x < board_size and 0 <= y < board_size:
                        if A[x][y] > 0:
                            safe += 1
                if safe < 3:
                    melt_ice.append([r,c])

    for r, c in melt_ice:
        A[r][c] -= 1
    return A

new_board = []
for stage in stages:
    new_board = firestorm(stage, board)
    board = new_board

# visited = [[0]*board_size for _ in range(board_size)]
# for r in range(0, board_size):
#     for c in range(0, board_size):
#
#
# def bfs(A, x, y, visited):
#     lump = 0
#     q = deque([0,0])
#     while q:
#         for i in range(4):
#             x = r + dx[i]
#             y = c + dy[i]
#             if 0 > x or x >= board_size or 0 > y or y >= board_size:
#                 continue
#             if visited[x][y] == 0 and new_board[x][y] > 0:
#                 visited[x][y] = 1
#                 lump
#                 q.append([x,y])
#     return lump

ice = 0
for i in range(board_size):
    ice += sum(new_board[i])

print(ice)
# print(lump)


