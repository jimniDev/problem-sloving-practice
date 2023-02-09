import sys
from bisect import bisect_left
read = sys.stdin.readline

def eat(N, A, M, B):
    A.sort()
    B.sort()
    cnt = 0
    for a in A: #A가 먹는 거임
        cnt += bisect_left(B, a)
    return cnt

ans = []
T = int(input())
for _ in range(T):
    N, M = map(int, read().split())
    A = list(map(int, read().split()))
    B = list(map(int, read().split()))
    ans.append(eat(N, A, M, B))

for i in ans:
    print(i)