# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque


def input_data():
	readl = sys.stdin.readline
	N, M = map(int, readl().split())
	infos = [list(map(int, readl().split())) for _ in range(M)]
	return N, M, infos

sol = -1

# 입력받는 부분
N, M, infos = input_data()
dp = [[1e9 for _ in range(N+1)] for _ in range(N+1)]
for a, b, dis in infos:
	dp[a][b] = dis
	dp[b][a] = dis
for i in range(1, N+1):
	dp[i][i] = 0

# 여기서부터 작성
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

min_far_dis = 1e9
for i in range(1, N+1):
	min_far_dis = min(min_far_dis, max(dp[i][1:]))
	 
# 출력하는 부분
print(min_far_dis)
