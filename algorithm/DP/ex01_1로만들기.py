#백준 1463

#dp
#작은문제 -> 큰문제 bottom up방식, +1은 연산횟수 세기위해
#-1 할때 : f(n) = f(n-1) + 1  
#//3 할때 : f(n) = f(n//3) + 1
#//2 할때 : f(n) = f(n//2) + 1

#숫자 1로부터 n 으로 가는 가장 빠른 방법 세기

n = int(input())
dp = [0]*(n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1 # -1 하는경우
    if i % 3 == 0: # 3으로 나눠지는경우
        dp[i] = min(dp[i], dp[i//3] + 1) 
    if i % 2 == 0: # 2로 나눠지는경우
        dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[n])


#BFS - 시간초과!!

# from collections import deque

# N = int(input())

# def BFS(x):
#     cnt = 0
#     Q = deque([(x,cnt)])
#     while(Q):
#         x,cnt = Q.popleft()
#         if x == 1:
#             return cnt
#         if x % 3 == 0:
#             Q.append([x//3, cnt+1])
#         if x % 2 == 0:
#             Q.append([x//2, cnt+1])
#         Q.append([x-1,cnt+1])

# print(BFS(N))


    


    
