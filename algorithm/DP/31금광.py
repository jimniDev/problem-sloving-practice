# 행 안에서 오른쪽 위, 오른쪽, 오른쪽 아래로만 갈수있다!
# 왜 행 내 최대값으로 생각했담? 

for tc in range(int(input())):
    n,m = map(int, input().split())
    arr = list(map(int, input().split()))

    dp = []
    index = 0
    for i in range(n):
        dp.append(arr[index:index + m])
        index += m
    
    for j in range(1,m):
        for i in range(n):
            #왼쪽위
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            #왼쪽 아래
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            #왼쪽
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left, left_down)
    
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1]) #마지막열에서 최대값 출력

    print(result)
            
