import sys
input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dir_change = (N-2)*2 + 3
repeat = 1
dir = [(0,-1), (1,0), (0,1), (-1,0)] # 0좌 1하 2우 3상
left_dust = [[-2, 0], [-1, -1], [-1, 0], [-1, 1], [0,-2], [1, -1], [1, 0], [1, 1], [2,0]]
dust_dir = [[] for _ in range(4)]
dust_amount = [0.02, 0.1, 0.07, 0.01, 0.05, 0.1, 0.07, 0.01, 0.02]
dust_dir[0] = left_dust

for i in range(1,4): #좌: y기준 2 10 7 1 5 10 7 1 2 순
    if i == 1: #하: 0,1 swap, 0*(-1)
        down_dust = []
        for d in left_dust:
            down_dust.append([d[1]*(-1), d[0]])
        dust_dir[1] = down_dust
    if i == 2: #우: *(-1)
        right_dust = []
        for d in left_dust:
            right_dust.append([d[0]*(-1), d[1]*(-1)])
        dust_dir[2] = right_dust
    if i == 3: #상: 0,1 swap, 1*(-1)
        up_dust = []
        for d in left_dust:
            up_dust.append([d[1], d[0]*(-1)])
        dust_dir[3] = up_dust

current = [(N//2, N//2)]
out = 0

def spread(board, x, y, current, d):
    spread_out = 0
    cur_x = x + dir[d][0]
    cur_y = y + dir[d][1]
    a_x = cur_x + dir[d][0]
    a_y = cur_y + dir[d][1]

    y_dust = board[cur_x][cur_y]
    a_dust = y_dust
    for k in range(len(dust_amount)):
        spread_x = cur_x + dust_dir[d][k][0]
        spread_y = cur_y + dust_dir[d][k][1]
        if 0 <= spread_x < N and 0 <= spread_y < N:
            board[spread_x][spread_y] += int(y_dust*dust_amount[k])
        else:
            spread_out += int(y_dust*dust_amount[k])
        a_dust -= int(y_dust * dust_amount[k])

    if 0 <= a_x < N and 0 <= a_y < N:
        board[a_x][a_y] += a_dust  # y 모래 a로
    else:
        spread_out += a_dust
    board[cur_x][cur_y] = 0
    current.append((cur_x, cur_y))
    return spread_out

for i in range(dir_change): # i%4 = 0좌 1하 2우 3상
    if i % 2 == 1: #홀수번째면
        for j in range(repeat):
            x, y = current.pop()
            out += spread(board, x, y, current, i%4) #모래이동
        if repeat != N-1: #마지막에 3번할차례아니면
            repeat += 1
    else:
        for j in range(repeat):
            x, y = current.pop()
            out += spread(board, x, y, current, i % 4) # 모래이동
print(out)

