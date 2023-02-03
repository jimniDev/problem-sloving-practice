def fillBox(n) :
    '''
    2 x n 의 상자를 2 x 1 의 블럭으로 채우는 경우의 수를 1,000,000,007로 나눈 나머지를 반환하는 함수를 작성하세요.
    '''
    if n == 1:
        return 1

    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2 #이걸 할려면 DP 배열을 n+1 로하면안됨~! or 작은값은 미리 리턴

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]%1000000007