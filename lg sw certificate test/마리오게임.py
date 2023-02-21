import sys
read = sys.stdin.readline

n =  int(input())
M = list(map(int, read().rstrip().split()))
dp = [0 for _ in range(n)]

increase_flag = True
for i in range(len(M)):
	# print(i, increase_flag)
	if increase_flag: # + 차례
		if i == n-1: # 마지막 원소일 경우 걍 더함
			dp[i] = dp[i-1] + M[i] 
		else:
			if M[i] >= M[i+1]: # 뒤에거보다 크면 더함
				if i == 1:
						dp[i] = M[i]
				else:
					dp[i] = dp[i-1]+M[i]
				increase_flag = False
			else:
				dp[i] = dp[i-1] #변화X
	else: # - 차례
		if i==n-1: #마지막 원소면 안빼고 마무리
			dp[i] = dp[i-1]
			continue
		if M[i] <= M[i+1]: #뒤에거보다 작으면 빼줌
			dp[i] = dp[i-1] - M[i]
			increase_flag = True
		else:
			dp[i] = dp[i-1] #변화X
	# print(dp)
	
print(dp[n-1])
			