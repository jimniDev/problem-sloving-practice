import sys
from bisect import bisect
read = sys.stdin.readline

n,h = map(int, read().split())
bottom = []
top = []

for i in range(n):
    if i % 2 == 0:
        bottom.append(int(read())) # 석순
    else:
        top.append(int(read())) # 종유석

top.sort()
bottom.sort()

min_val = 1e9
cnt = 0
for i in range(h):
    bottom_cnt = n//2 - bisect(bottom, i) # h < b 면 파괴, len - i가 위치할 인덱스(리턴값)파괴한 갯수
    top_cnt = n//2 - bisect(top, h-1-i)   # h-1-i < t 면 파괴, len- 리턴값이 파괴한 갯수
    # print(i, bottom_cnt, top_cnt)
    cur = bottom_cnt + top_cnt
    if cur < min_val:
        min_val = cur
        cnt = 1
    elif cur == min_val:
        cnt += 1

print(min_val, cnt)




