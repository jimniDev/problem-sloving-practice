## -1먼저하는 경우가 답인 예시가 있으므로 그리디 X

## BFS
# from collections import deque
# n = int(input())
# visited = [0]*(n+1)
# q = deque([n])

# while q:
#     x = q.popleft()
#     if x == 1:
#         break
#     if x%3 == 0 and visited[x//3]==0: #방문한적 없다면 방문
#         nx = x//3
#         q.append(nx)
#         visited[nx] = visited[x]+1 #연산횟수+1
#     if x%2 == 0 and visited[x//2]==0:
#         nx = x//2
#         q.append(nx)
#         visited[nx] = visited[x]+1
#     if visited[x-1]==0:
#         nx = x-1
#         q.append(nx)
#         visited[nx] = visited[x]+1
#     # 방문한적 있는 숫자는 나중 방문이 무조건 연산횟수가 더 크기 때문에 들릴 필요X
# print(visited[1])
# #목표인 1의 최소연산횟수 출력
            
##DP
n = int(input())
dp = [0]*(n+1)
# 1부터 채우는 상향식 DP
for i in range(2, n+1): # 1입력시 1되는 연산횟수 어차피 0 이므로 2부터 시작
    dp[i] = dp[i-1] + 1 # -1 하는 경우
    if i%3 == 0: 
        #3나누어 떨어질때, min(위에서-1일시 연산횟수, i//3이 1이되는데 최소횟수 +1) 중 최소 저장
        dp[i] = min(dp[i], dp[i//3]+1) 
    if i%2 == 0:
        dp[i] == min(dp[i], dp[i//2]+1) 
    print(dp)

print(dp[n]) # n이 1이 되는데 필요한 연산 최소 횟수