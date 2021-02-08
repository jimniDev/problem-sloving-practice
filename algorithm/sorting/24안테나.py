#중간값이 거리합최소위치
 
n = int(input())
houses = sorted(list(map(int, input().split())))
print(houses[n//2 -1])
