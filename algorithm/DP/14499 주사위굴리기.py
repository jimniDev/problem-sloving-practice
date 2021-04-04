#14499 주사위굴리기.py
# M = [list(map(int, input().split())) for _ in range(n)]
# [[0, 2], [3, 4], [5, 6], [7, 8]]

# M = [input().split() for _ in range(n)]
# [['0', '2'], ['3', '4'], ['5', '6'], ['7', '8']]

n, m , x, y, k = map(int, input().split())
M = [input().split() for _ in range(n)]
order = list(map(int, input().split()))
dice = [0 for _ in range(7)]

print(M)

dx = [0, 0, -1, 1] #동서북남
dy = [1, -1, 0 ,0]

for i in order:

    nx = x + dx[i-1]
    ny = y + dy[i-1]
    #벗어난경우 
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

    if i == 1:
        dice[6], dice[4], dice[1], dice[3] = dice[3], dice[6], dice[4], dice[1]
    elif i == 2:
        dice[6], dice[3], dice[1], dice[4] = dice[4], dice[6], dice[3], dice[1]
    elif i == 3:
        dice[6], dice[5], dice[1], dice[2] = dice[2], dice[6], dice[5], dice[1]
    else:
        dice[6], dice[2], dice[1], dice[5] = dice[5], dice[6], dice[2], dice[1]

    if M[nx][ny] == 0: #이미방문
        M[nx][ny] = dice[6]
    else: # 처음방문
        dice[6] = M[nx][ny]
        M[nx][ny] = 0 

    x, y = nx, ny
    print(dice[1])