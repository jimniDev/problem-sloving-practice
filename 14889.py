import sys
from itertools import combinations

read = sys.stdin.readline
n = int(read())
S = [list(map(int, read().split())) for _ in range(n)]
arr = list(range(n))
min_sub = 1e9

for start in combinations(arr, n//2):
    link = list(set(arr) - set(list(start)))
    print(link)
    link_p = 0
    stat_p = 0 
    for comb in combinations(start, 2):
        i, j = comb
        stat_p += (S[i-1][j-1] + S[j-1][i-1])
    
    for link in combinations(link, 2):
        i, j = comb
        link_p += (S[i-1][j-1] + S[j-1][i-1])
    
    min_sub = min(min_sub, abs(link_p-stat_p))

print(min_sub)
        
