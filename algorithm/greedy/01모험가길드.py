#1 모험가길드
# 5
# 2 3 1 2 2

# 아이디어1
# 최대한많은그룹 - 공포도 높은사람부터해결
# 3 2 2 2 1 내림차순 정렬한다음, 수만큼 인덱스 돌고 그룹++
# 다음인덱스에서 수만큼 돌고 그룹++
# 끝나면 그룹출력

#리스트.sort(reverse=True)

n = int(input())
a = list(input().split())
group = 0
index = 0
a.sort(reverse=True)

for i in range(len(a)):
    if (index == i):
        index += int(a[i])
        group+=1
    else:
        continue

print(group)

#45분 - 이아이디어에서 잘못된점은?
#

#아이디어2 - 답안
#1 2 2 2 3오름차순 정렬하여 공포도낮은사람부터 묶기
#최소모험가로 그룹구성 => 최대그룹수

n = int(input())
a = list(input().split())
group = 0
mem = 0

for i in a:
    mem += 1
    if mem >= i: #현재 그룹의 모험가수가 현재 공포도 이상이면 
       group += 1 #그룹결성
       mem = 0 #현재 그룹의 모험가수 초기화

print(group)

