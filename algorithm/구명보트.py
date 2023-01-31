#구명보트.py

# def solution(people, limit):
#     answer = 0
#     people.sort()
#     dp = [[0,0] for _ in range(len(people)+1)]
#     # print(dp)
#     dp[1] = [1,people[0]] 
#     for i in range(2, len(people)+1):
#         dp[i][1] = dp[i-1][1]+people[i-1]
#         if i%2 == 0:
#             if dp[i][1]//(i/2) <= limit:
#                 dp[i][0] = dp[i-1][0]
#             else:
#                 dp[i][0] = dp[i-1][0]+1
#         else:
#             dp[i][0] = dp[i-1][0]+1
#     # print(dp)
#     return dp[len(people)][0]

def solution(people, limit):
    answer = 0
    people.sort()
    s = 0
    e = len(people)-1
    while(s<=e):
        if people[s]+people[e] <= limit:
            s +=1
            e -=1
        else:
            e -=1
        answer += 1
    return answer