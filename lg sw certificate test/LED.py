import sys
from collections import deque
def input_data():
	readl = sys.stdin.readline
	N = int(readl())
	led = list(map(int, readl().split()))
	return N, led

# 가장 긴 onoff 구간은, 10, 01 기준으로 세트를 나눴을때 가운데 세트 반전했을때
# 세트 3개씩 묶어 큐에 저장하면서 길이 비교 - Sliding window

N, led = input_data()
sets = deque()
cur = []
sets_len = 0
max_len = 0
for i in range(N):
	cur.append(led[i])
	if i <= N-2 and abs(led[i+1] - led[i]) == 1: #파트이어짐
			continue	
	# print(cur)
	sets.append(cur)
	sets_len += len(cur)
	cur = []
	# 이걸 뒤로 보내는게 더 많이맞네..?
	if i== N-1 and len(sets) < 3:
		max_len = sets_len
	if len(sets) == 3: #세트 3개 모으면 window 이동 
		max_len = max(sets_len, max_len) # 정답갱신
		sets_len -= len(sets.popleft()) # 맨앞 세트 빼고 길이 갱신
	
print(max_len)
		
		

