# 15685드래곤커브.py
# 커브의 규칙찾기. 진행방향이 0 01 0121 01212321 로 배열리버스+1 반복
n = int(input())
m = [[1 for _ in range(101)] for _ in range(101)]

# 0우 1상 2좌 3하
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(n):
    x, y, d, g = map(int, input().split())
    curve = [d]
    for _ in range(g):
        curve += [(i+1)%4 for i in curve[::-1]]
    m[y][x] = 0
    for c in curve:
        nx = x + dx[c]
        ny = y + dy[c]
        m[ny][nx]=0
        x, y = nx, ny

ans = 0
for i in range(100):
    for j in range(100):
        if m[i][j] + m[i+1][j] + m[i][j+1] + m[i+1][j+1] == 0:
            ans += 1
print(ans)