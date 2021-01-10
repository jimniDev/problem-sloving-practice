#04 만들수없는금액
# N개의 동전을 이용해 만들수없는 금액중최소
# 입력
# 동전갯수 N
# 화폐단위 N개

#아이디어
#1~합까지 비교 - 없으면 합+1이 최소
#합경우의수 어떻게? 오름차순정렬 1 1 2 3 9,
#1,2,3..n-1,n개 합

#최대단위 > n이면 답 =< 최대단위
#최대단위 < n이면 답 =< n 2222 4 1111 4 1231 4
# 같으면  합+1이 답 1234 4  1124 4 
n = int(input())
data = list(map(int, input().split()))
#data.sort()
ans = 1
if max(data) > n:
    for i in range(1, max(data)+1):
        if i not in data:
            ans = i
            break
elif max(data) == n:
    ans = sum(data)+1
else:
    for i in range (1, n+1):
        if (i not in data) and i != n:
            ans = i
            break
    ans = sum(data)+1
print(ans)

#45분 t-t


#문제점: 왜그리디적사고를하지않고 구데기로 문제를푸냐?
#답
#오름차순정렬 그리디
# target 만큼 만들수있다 =  1~target-1 까지의 모든 금액 만들수있다 -> 업데이트

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x
print(target)