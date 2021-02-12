#떡개수 n, 요청한 떡길이 m
import sys

n, m = map(int, input().split())
cakes = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = cakes[0]

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for cake in cakes:
        if cake - mid > 0:
            total += (cake - mid)
    if total < m:
        end = mid - 1
    else:
        result = mid  # 최대한 덜잘랐을때가 정답
        start = mid + 1
    
print(result)
        

