n = int(input())
t = []
p = []
dp = [0]*(n+1)
max_value = 0

for i in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n-1, -1, -1):
    time = t[i] + i
    # 상담이 시간 안에 끝나는 경우
    if time <= n:
         dp[i] = max(p[i] + dp[time], max_value)
         max_value = dp[i]
    # 상담이 기간을 벗어가는 경우
    else:
        dp[i] = max_value

print(max_value)

#dp[i] = i번째 날부터 마지막날까지 낼 수 있는 최대 이익
#dp[i] = max(p[i] + dp[t[i] + i], max_vaule) max_value
