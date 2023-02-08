import sys
from collections import deque
def input_data():
	readl = sys.stdin.readline
	loop = readl().strip()
	return loop
# 입력 받는 부분
loop = input_data()

#코드작성
q = deque(loop)
depth = 0 

def do_loop(depth): # < 다음부터 받음
	global q
	stack = [] # depth 마다 새로 선언
	
	q.popleft() # < 제거
	num = int(q.popleft()) # 횟수저장 
	
	while q:
		x = q.popleft()
		if x == '>': # 닫는거 만나면 쌓은 스택 리턴
			break
		elif x == '<': # 여는거 만나면 새 depth
			q.appendleft(x) # < 다시 넣고
			moved = do_loop(depth+1) # 새 depth
			stack.append(moved)  # 리턴한 결과 스택 추가
		else:
			stack.append(x) # 알파벳은 스택 추가
	#이시점에 stack 다 채워짐
	return ''.join(num*stack) # 횟수만큼 반복해서 리턴 (문자열)

ans = do_loop(depth)
print(ans)

		