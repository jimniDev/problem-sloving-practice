from collections import deque
N, S, M = map(int, input().split())
ppl = list(range(1, N+1)) # 1~N
order = list(range(N)) # 0~N-1

s = S-1
for i in range(N):
	# print(ppl)
	end = (s+M)%len(ppl)
	if end == 0:
		order[i] = ppl.pop()
	else:
		left = ppl[:end]
		right = ppl[end:]
		order[i] = left.pop()
		ppl = right + left	
	s = 0
for i in order:
	print(i, end= ' ')
		
		

