import sys
from collections import Counter
N, M = map(int, sys.stdin.readline().split())
sum_arr = []

for n in range(1, N+1):
    for m in range(1, M+1):
        sum_arr.append(int(n+m))

sum_cnt = sorted(Counter(sum_arr).items(), key = lambda x: (-x[1], x[0]))
max_val = sum_cnt[0][1]
for k, v in sum_cnt:
    if v == max_val:
        print(k)

