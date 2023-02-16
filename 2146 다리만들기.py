from itertools import combinations
from collections import deque
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
A = [list(map(int, read().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
dr, dc = [1,-1,0,0], [0,0,1,-1]
closes = []

def find_land(r, c, num):
    close = []
    visited[r][c] = 1
    A[r][c] = num #여기 초기화 안해줘서 섬크기1x1 일떄 안됐음
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr <n and 0 <= nc <n:
            if A[nr][nc] == 0 and (r,c) not in close:
                visited[nr][nc] = 1
                close.append((r,c))
            if A[nr][nc] == 1 and visited[nr][nc] == 0:
                A[nr][nc] = num
                visited[nr][nc] = 1
                close += find_land(nr,nc,num)
    return close

def get_distance(q, val): 
    global n,A
    res = 1e9
    visited_b = [[0 for _ in range(n)] for _ in range(n)]
    while q:
        r,c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and visited_b[nr][nc] == 0:
                if A[nr][nc] < val:
                    visited_b[nr][nc] = visited_b[r][c]
                    res = min(res, visited_b[nr][nc])
                if A[nr][nc] == 0:
                    visited_b[nr][nc] = visited_b[r][c] + 1
                    q.append((nr,nc))

    return res

num = -1
for r in range(n):
    for c in range(n):
        if A[r][c] == 1 and visited[r][c] == 0:
            closes.append(find_land(r,c, num)) # 섬 개수만큼 close 배열들 생김
            num -= 1
# print(A)

# print(closes)
# [
# -1 [(2, 0), (1, 1), (3, 2), (4, 3), (1, 3), (2, 3), (3, 4), (2, 2), (0, 2)],
# -2 [(0, 7), (2, 8), (5, 9), (4, 9), (3, 9), (1, 8)],
# -3 [(8, 4), (8, 5), (7, 5), (8, 6), (7, 4)]
# ]

land_cnt = len(closes)
min_dis = 1e9

for i in range(land_cnt): # 섬갯수만큼
    # 더 큰 인덱스 (더 작은 음수 값) 에 대해서만 탐색
    # for point in closes[i]:
    #     # 섬 별 close 중 2개로  a ~ b 최단거리 구하기
    #     # print(a,b)
    point = deque(closes[i]) #한 섬 전체를 큐에 넣어서 bfs
    dis = get_distance(point, -(i+1))
    # print(-(i+1), dis)
    min_dis = min(min_dis, dis)

print(min_dis)


    # for land_pair in combinations(closes, 2): # 섬 중에 2개 쌍
    #     close1, close2 = land_pair
    #     for a in close1 : 
    #         for b in close2:
    #             # 섬 별 close 중 2개로  a ~ b 최단거리 구하기
    #             # print(a,b)
    #             dis = abs(a[0]-b[0]) + abs(a[1]-b[1]) -1
    #             min_dis = min(min_dis, dis)
# print(min_dis)


# 시간초과 BFS

# land_cnt = len(closes)
# min_dis = 1e9
# for land_pair in combinations(closes, 2): # 섬 중에 2개 쌍
#     close1, close2 = land_pair
#     for a in close1 : 
#         for b in close2:
#             # 섬 별 close 중 2개로  a ~ b 최단거리 구하기
#             # print(a,b)
#             dis = get_distance(a, b)
#             min_dis = min(min_dis, dis)

# print(min_dis)

    

