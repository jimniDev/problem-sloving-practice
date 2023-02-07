import sys
read = sys.stdin.readline

N, M = map(int, read().split())
money = [int(read()) for _ in range(N)]

# 완탐 = N 10만 x 돈 1만  
# log(1만) = 13
# 둘중 하나를 줄여야 => 이분탐색 !!!


max_ = max(money)
l = min(money) # 예산 중 최소 값 -> 최대출력: N번
r = sum(money) # 예산 합 -> 최소출력: 1번

while l <= r:
    mid = (l+r)//2
    cur = mid 
    cnt = 1
    for i in range(N):
        if cur < money[i]:
            cur = mid #돈 다시 mid 원
            cnt += 1 #인출횟수++
        cur -= money[i]

    if cnt > M  or mid < max_: #다돌았는데 M번 이상 인출 or 예산최대값 보다 작아
        l = mid + 1
    else: # 최소값이니까 되는 경우 줄인다.
        r = mid - 1
        k = mid
    
print(k)