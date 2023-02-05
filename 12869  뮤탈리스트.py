from collections import deque
from itertools import permutations

n = int(input())
scv = list(map(int, input().split()))
visited = []

method = list(permutations([-9,-3,-1], 3))
q = deque()
q.append([scv, 0])
visited.append(scv)

while q:
    svc, cnt = q.popleft() #scv배열, die, cnt
    # print(svc, cnt)
    if sum(svc) == 0:
        break
    for m in range(6):
        n_svc = [0]*len(svc)
        for i in range(len(svc)):
            n_svc[i] = svc[i] + method[m][i]
            if n_svc[i] <=0:
                n_svc[i] = 0
        if n_svc not in visited:
            q.append([n_svc, cnt+1])
            visited.append(n_svc)
print(cnt)

