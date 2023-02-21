import sys
import heapq

readl = sys.stdin.readline
N = int(input())
customers = []
for _ in range(N):
	P, T = map(int,readl().split())
	customers.append([-P, T])

customers = sorted(customers, key=lambda x: (x[0], x[1]))
# print(customers)
heapq.heapify(customers)
confirm = [0 for _ in range(10001)]

while customers:
	price, t = heapq.heappop(customers)
	if t >= 1:
		if confirm[t] == 0:
			confirm[t] = price
		else:
			if t >= 2:
				heapq.heappush(customers, [price, t-1])

# print(confirm)
print(-sum(confirm))