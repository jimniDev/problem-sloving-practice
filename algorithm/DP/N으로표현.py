# def solution(N, number):
    
#     dp = [8]*(int(str(N)+str(N)))
#     print(len(dp))
    
#     dp[0] = 2
#     dp[1] = 2
#     dp[N] = 1
#     for i in range(2, number+1):
#         q = i // N
#         r = i % N
#         if r == 0:
#             dp[i] = q
#         else:
#              dp[i] = min(dp[i-1]+1, dp[N*q] + dp[r], dp[N*(q+1)] + dp[N-r]) 
#         print(i, dp[i])

#     # print(dp[number])
#     if dp[number] >= 8:
#         return -1
#     else:
#         return dp[number]

def solution(N, number):
    if N == number:
        return 1
        
    # 1. [ SET x 8 ] 초기화
    s = [ set() for x in range(8) ] 

    # 2. 각 set마다 기본 수 "N" * i 수 초기화
    for i,x in enumerate(s, start=1):
        x.add( int( str(N) * i ) )

    # 3. n 일반화
    #   { 
    #       "n" * i U 
    #       1번 set 사칙연산 n-1번 set U
    #       2번 set 사칙연산 n-2번 set U
    #       ...
    #       n-1번 set 사칙연산 1번 set, 
    #    } 
    # number를 가장 최소로 만드는 수 구함.
    for i in range(1, 8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)

        if  number in s[i]:
            answer = i + 1
            break

    else:
        answer = -1

    return answer

N, num = map(int, input().split())
print(solution(N, num))

