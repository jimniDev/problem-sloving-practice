import sys

readl = sys.stdin.readline
N = int(readl())
A = [int(x) for x in readl().split()]


min_val = 1e9
l, r = 0, len(A)-1
ans = l, r

while l < r:
	cur = A[l] + A[r]
	# print(l, r, cur)
	if abs(cur) < min_val: # 더 작으면 답 갱신
		ans = l,r 
		min_val = abs(cur)
		
	if cur == 0:
		break
	elif cur < 0:
		l += 1
	else:
		r -= 1

# print('답', ans)
print(ans[0], ans[1])

