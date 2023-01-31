import heapq
import sys

read = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
  x = int(read().rstrip())
  if x == 0:
    #제일 작은 값 출력
    if len(heap) == 0:
      print(0)
    else:
      print(heapq.heappop(heap))
  else:
    heapq.heappush(heap, x)
