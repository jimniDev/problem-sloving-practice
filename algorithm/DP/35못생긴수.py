# 2,3,5만을 소인수로 가지는수 
# 1은 못생긴수
# 1 2 3 4 5 6 7 8 9 10 12 15 ...
# n번쨰 못생긴수 출력



N = int(input())

dp = [0] * N
dp[0] = 1

i2, i3, i5, min2, min3, min5 = 0, 0, 0, 2, 3, 5
for i in range(1, N):
    dp[i] = min(min2, min3, min5)
    if dp[i] == min2:
        i2 += 1
        min2 = dp[i2] * 2
    if dp[i] == min3:
        i3 += 1
        min3 = dp[i3] * 3
    if dp[i] == min5:
        i5 += 1
        min5 = dp[i5] * 5

print(dp[N - 1])
    