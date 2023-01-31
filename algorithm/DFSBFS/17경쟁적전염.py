#17경쟁적전염
# 1~K 번 바이러스, 1초마다 상하좌우 낮은번호우선 증식, 이미있으면 X
#  (1 ≤ N ≤ 200, 1 ≤ K ≤ 1,000)
# S초후에 (x,y)에 존재하는 바이러스 종류 출력, 없으면 0
#  (0 ≤ S ≤ 10,000, 1 ≤ X, Y ≤ N)

#BFS로 Queue


from collections import deque

n, k = map(int, input().split())
lab = []
for i in range(n):
    lab.append(list(map(int, input().strip().split())))

S, X, Y = map(int, input().split())
virus = deque()
time = 0
for i in range(n): # 바이러스 저장
    for j in range(n):
        if lab[i][j] != 0:
            virus.append([lab[i][j], i, j, time]) #바이러스 번호, x, y, 초
virus = deque(sorted(virus, key=lambda x: x[0])) #낮은번호의 바이러스가 먼저오게 정렬

dr = [-1,0,1,0] # 위아래 row 단위로 이동
dc = [0,1,0,-1] # 좌우 column 단위로 이동


while len(virus)>0:
    virus_num, r, c, time = virus.popleft()
    if time == S:
        break
    for dir in range(4):
        n_r = r+dr[dir]
        n_c = c+dc[dir]
        if n_r >= 0 and n_c >=0 and n_r < n and n_c < n : # 범위를 벗어나지 않을때
            if lab[n_r][n_c] == 0 :
                lab[n_r][n_c] = virus_num
                virus.append([virus_num, n_r, n_c, time+1])

print(lab[X-1][Y-1])
