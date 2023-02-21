import sys
readl = sys.stdin.readline

n = int(readl())
A = []
minr, minc, maxr, maxc = n,n,-1,-1
color = [[minr, minc, maxr, maxc] for _ in range(10)]
repaint = [-1 for _ in range(10)]

for r in range(n):
	A.append(list(map(int, readl().strip())))
	for c in range(n):
		if A[r][c] > 0:
			cur = color[A[r][c]]
			minr, minc = min(r, cur[0]), min(c, cur[1])
			maxr, maxc = max(r, cur[2]), max(c, cur[3])
			color[A[r][c]] = [minr, minc, maxr, maxc]
			repaint[A[r][c]] = 0 #책깔이 있다면 한번칠함으로 초기호ㅏ
# print(color)
# min ~ max까지 원래영역 전체 돌면서 repaint 배열 변경
for i in range(1, len(color)):
	minr, minc, maxr, maxc = color[i]
	if minr == n:
		continue
	for r in range(minr, maxr+1):
		for c in range(minc, maxc+1):
			if repaint[A[r][c]] == 0:
				if A[r][c] != i: # 덮어지지않음
					repaint[A[r][c]] = 1 # 덧칠된 색깔
# print(repaint)
ans  = 0
for i in repaint:
	if i == 0:
		ans += 1
print(ans)

