# i,j 같은팀 -> 팀 += (Sij + Sji)
# 스타크, 링크팀 능력차 최소값 출력

# N(4 ≤ N ≤ 20, N은 짝수)

# 4
# 0 1 2 3
# 4 0 5 6
# 7 1 0 2
# 3 4 5 0

from itertools import combinations

N = int(input())
ability = [input().split() for i in range(N)]
# print(list(combinations(range(1, N+1), N//2)))
teams = []

for team in list(combinations(range(1, N+1), N//2)): # 팀 나누는 경우의수
    team_sum = 0
    for s in list(combinations(team, 2)): # 능력치 계산
        i, j = s[0], s[1]
        s_sum = int(ability[i-1][j-1]) + int(ability[j-1][i-1])
        team_sum += s_sum
    #print(team, team_sum)
    teams.append((team, team_sum))
# print(teams)

sub_min = int(1e9)
for i in range(len(teams)//2): # 팀 사이 능력치 차 계산 
    current =abs(teams[i][1] - teams[len(teams)-1 - i][1])
    # print(sub_min, current)
    sub_min = min(sub_min, current)

print(sub_min)