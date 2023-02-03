n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)] # i 일까지 최대 금액


for i in range(n):
    dp[i]= max(dp[i], dp[i-1])
    # 전날까지의 금액이 더 클수 있으므로 더 큰 값으로 갱신
    if i+arr[i][0] <= n:
        dp[i+arr[i][0]] = max(dp[i+arr[i][0]], dp[i] +arr[i][1])
        # i일에 시작한 일이 끝나는 날짜까지의 최대 금액 
        # = i-1일 까지 최대 금액 + i일 금액, 이전에 기록된 값 
    print(dp)
print(max(dp))
