import sys

def input_data():
	readl = sys.stdin.readline
	n = int(readl())
	a = [list(map(int, readl().split())) for y in range(n)]
	return n, a


# 입력
# N : 장비에 장착된 노즐의 가로, 세로 개수
# A : 각 노즐의 오염도 정보
sol = -1
N, A = input_data()

# 코드를 작성하세요
row_max = 0
col_max = 0
# 1. 행 돌면서 홀수열 or 짝수열 선택 = 옆으로 붙는게 없음
for r in range(N):
	tmp = [0,0]
	for c in range(N):
		tmp[c%2] += A[r][c]
	row_max += max(tmp)

# 2. 열 돌면서 홀수행 or 짝수행 선택 = 위아래로 붙는게 없음
for c in range(N):
	tmp = [0,0]
	for r in range(N):
		tmp[r%2] += A[r][c]
	col_max += max(tmp)
# 출력
print(max(row_max, col_max))