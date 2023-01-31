#공유기설치
# 5 3
# 1
# 2
# 8
# 4
# 9

import sys
n,m = map(int, input().split())
houses = sorted([int(sys.stdin.readline().rstrip()) for i in range(n)])

start = 1
end = houses[-1] - houses[0]

while start <= end:
    mid = (start + end) // 2
    value = houses[0]
    count = 1
    for i in range(1,n):
        if houses[i] >= value + mid:
            value = houses[i]
            count += 1
    if count >= m:
        start = mid +1
        result = mid
    else:
        end = mid-1

print(result)