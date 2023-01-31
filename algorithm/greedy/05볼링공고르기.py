#05 볼링공고르기
# 서로무게다른 볼랑공 고르는 조합

#아이디어
#오름차순정렬 
# 13232 12233 -> 3 5c2 - 2
# 11122 5c2 - 3c2 - 2c2 

import math

N, M = map(int, input().split())
balls = list(map(int, input().split()))
balls.sort()
weight_list = [0]*(M+1)
same = 0
for i in balls:
    weight_list[i] += 1
#print(weight_list)
for j in weight_list:
    if j >= 2:
        same += math.factorial(j)/(math.factorial(j-2)*2) #jC2
print(math.factorial(N)/(math.factorial(N-2)*2) - same)