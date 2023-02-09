import sys

def InputData():
	readl = sys.stdin.readline
	N = int(readl())
	H = [ int(readl()) for i in range(N) ]
	return N, H

# 입력
# N: 건물 수
# H: 건물 높이
N, H = InputData()
ans = -1

stack = [] # 내자신이 보이는 건물 저장
visible = [0 for _ in range(N)]

for i in range(N):
	while stack: 
		if stack[-1] <= H[i]: # 스택 탑이 나보다 작으면  = 나보다 작은 서쪽 건물
			stack.pop() # 그건물은 내 옥상 못봄
		else:
			break # 스택탑이 나보다 커 = 그럼 내 옥상이 보임
	stack.append(H[i]) # 스택 비어있으면 나넣음 = 날 옥상 볼수잇는 건물이업듬
	visible[i] = len(stack)-1 # 나제외 나보이는 건물 갯수

# print(visible)
print(sum(visible))
			
			