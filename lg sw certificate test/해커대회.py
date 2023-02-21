import sys
import heapq
read = sys.stdin.readline

head = list(read().rstrip())
cmd = list(read().rstrip())

tail = []
for x in cmd:
	if x == 'L':
		if head: #head pop해서 tail 추가 / head가 비면 무시
			tail.append(head.pop())
	elif x == 'R':
		if tail: #tail pop해서 head 추가 / tail 비면 무시
			head.append(tail.pop())
	elif x == 'B':
		if head: #head pop / head가 비면 무시
			head.pop()
	else: #소문자 : head push
		head.append(x)
	# print(tail, '   ^   ', head)

for ele in head + list(reversed(tail)):
	print(ele, end='')

#heapq 풀이 (5/10, 5~9 틀림)

# for i in range(len(org), 0, -1):
# 	# print(-i, org[i-1])
# 	heapq.heappush(head, (-i, org[i-1]))

# tail = []
# for x in cmd:
# 	if x == 'L':
# 		if head: #q pop해서 stack 추가 / q가 비면 무시
# 			tail.append(heapq.heappop(head))
# 	elif x == 'R':
# 		if tail: #stack pop해서 q 추가 / stack 비면 무시
# 			heapq.heappush(head, tail.pop())
# 	elif x == 'B':
# 		if head: #q pop / q가 비면 무시
# 			heapq.heappop(head)
# 	else: #소문자
# 		if len(tail) > 0 and len(head) == 0:
# 			idx = tail[-1][0] - tail[-1][0]/2
# 		elif len(tail) == 0 and len(head) > 0:
# 			idx = head[0][0] + head[-1][0]/2
# 		else:
# 			idx = (head[0][0] + tail[-1][0])/2 
# 		heapq.heappush(head, (idx, x))
# 	# print(tail, '   ^   ', head)

# ans = []

# for ele in tail:
# 	ans.append(ele)
# while head:
#   ans.append(heapq.heappop(head))

# # for ele in tail:
# # 	ans.append(ele[1])
# # while head:
# #   ans.append(heapq.heappop(head)[1])

# for i in reversed(ans):
# 	print(i, end='')

	