from itertools import combinations
# 15686 치킨배달

# 0빈칸, 1집, 2치킨집
# 집 적어도 1개 존재 <= 2N
# m<= 치킨집 <= 13
# r, c 1부터
# 치킨거리: 집과 젤 가까운 치킨집
# 도시의 치킨거리 = sum(각각의 집 치킨거리) 
# N개중 도시 치킨거리를 최소로 만드는 치킨집 M개 선택

n, m = map(int, input().split())
A = []
chickens = []
houses = []
for r in range(1, n+1):
    A.append(list(map(int, input().split())))
    for c in range(1, n+1):
        if A[r-1][c-1] == 2:
            chickens.append((r,c))
        elif A[r-1][c-1] == 1:
            houses.append((r,c))

# print(A)
# print(chickens)
# print(houses)

min_dis_city = []
for chicken in combinations(chickens, m): #13c~
    #치킨집 선택 경우의수 하나씩
    dis_city = 0
    for h in houses: # 집별 최소 치킨거리 구하기
        min_dis = 1e9
        for c in chicken:
            cur_dis = abs(c[0]-h[0]) + abs(c[1]-h[1])
            min_dis = min(cur_dis, min_dis)
        dis_city += min_dis
    min_dis_city.append(dis_city)
print(min(min_dis_city))
