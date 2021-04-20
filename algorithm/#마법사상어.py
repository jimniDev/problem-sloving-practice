#마법사상어.py

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
M = [[[] for _ in range(n)] for _ in range(n)]
fires = []
for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    M[r-1][c-1].append([r-1, c-1, m, s, d]) # 0: 질량, 1:속력, 2:방향
    fires.append([r-1, c-1, m, s, d])

dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]  # 0 1 2 3 4 5 6 7 방향
d_0 = [0,2,4,6]
d_1 = [1,3,5,7]

for _ in range(k):
    for f in range(len(fires)): #이동
        r, c, m, s, d = fires[f]
        move_r, move_c = (r + dir[d][0]*s)%n, (c + dir[d][1]*s)%n
        M[move_r][move_c].append([move_r, move_c, m, s, d])
        M[r][c].remove([r, c, m, s, d])

    for i in range(n):
        for j in range(n):
            if len(M[i][j]) > 1:  # 2개이상이면
                m_sum, s_sum, d_arr = 0, 0, []
                for fire in M[i][j]: #[r, c, m, s, d]
                    m_sum += fire[2]
                    s_sum += fire[3]
                    if fire[4] % 2 == 0: d_arr.append(0) #짝
                    else: d_arr.append(1) #홀
                new_m = m_sum//5
                new_s = s_sum//len(M[i][j])
                if new_m == 0:
                    M[i][j] = []
                else:
                    if sum(d_arr) == 0 or sum(d_arr) == len(M[i][j]): #0246
                        spread_dir = d_0
                    else:
                        spread_dir = d_1
                    M[i][j] = []
                    for dd in spread_dir:
                        M[i][j].append([i, j, new_m, new_s, dd])
    fires = []
    for i in range(n):
        for j in range(n):
            if M[i][j] != []:
                fires += M[i][j]

ans = 0
for i in range(len(fires)):  # 이동
    ans += fires[i][2]
print(ans)





# def spread(M, fire):
#     for i in range(n):
#         for j in range(n):
#             if len(M[i][j]) > 1: # 2개이상이면
#
#
#
# def move(M, fire):
#     dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]  # 0 1 2 3 4 5 6 7 방향
#     while fire:
#         r, c, m, s, d = fire.popleft()
#         M[r][c] =
#         move_r = abs(5 - abs(r + dir[d][0])%4)
#         move_c = abs(5 - abs(c + dir[d][1])%4)
#         M[move_r][move_c].append([m,s,d])
#     return
#
#
#
#
#
#
#

