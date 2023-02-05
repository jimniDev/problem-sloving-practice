def eating(data) :
    '''
    각 날짜 별 음식의 선호도가 list로 주어질 때, 상훈이가 얻을 수 있는 선호도 총합의 최댓값을 반환하는 함수를 작성하세요.
    '''
    n = len(data)
    dp = [[0]*3 for _ in range(n)]

    for i in range(n):
        for j in range(3):
            for k in range(3): # 그전날 idx
                if j != k:
                    dp[i][j] = max(dp[i][j], dp[i-1][k])
            dp[i][j] += data[i][j]                 
    return max(dp[n-1])