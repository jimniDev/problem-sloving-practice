#바닥공사
#가로길이 N, 세로 2 직사각형
#1x2, 2x1, 2x2 로 덮는 경우의수

# n-1 까지 채워져있을때 1x2
# n-2 까지 채워져있을때 2x2 or 2x1 두개(=) -> 두가지 경우
# 점화식 dp[i] = dp[i-1] + dp[i-2] * 2

n = int(input())
dp = [0]*n
dp[0] = 1
dp[1] = 3

for i in range(2, n):
    dp[i] = dp[i-1] + dp[i-2] * 2

print(dp[n-1])
