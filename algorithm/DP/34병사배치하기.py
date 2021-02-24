# n = int(input())
# soldiers = list(map(int, input().split()))
# dp = [0]*n
# prev = soldiers[0]

# print(dp)
# for i in range(1, n): #두번째병사부터 비교
#     if soldiers[i] > prev:
#         dp[i] = dp[i-1] + 1  
#     else:
#         dp[i] = dp[i-1]
#     prev = soldiers[i]

# print(dp[n-1])

# 문제에서 정렬을 보면 이진탐색, 가장 긴 증가하는 부분수열, 감소수열 떠올리자

n = int(input())
soldiers = list(map(int, input().split()))
soldiers.reverse()
dp = [1]*n

for i in range(1, n): #두번째병사부터 비교
    for j in range(0, i):
        if soldiers[j] < soldiers[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))

