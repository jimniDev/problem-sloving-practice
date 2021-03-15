# 5 4
# 0 1 0 1 1
# 1 0 1 1 0
# 0 1 0 0 0
# 1 1 0 0 0
# 1 0 0 0 0
# 2 3 4 3

#p393
# 여행계획 도시들이 서로 같은 집합이면 YES

def find_parents(parent, x): #루트노드 찾을때까지 재귀
    if parent[x] != x:
        parent[x] = find_parents(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parents(parent, a)
    b = find_parents(parent, b)
    if a < b:
        parent[b]= a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            union_parent(parent, i+1, j+1)
    
plan = list(map(int, input().split()))

result = True
for i in range(m-1):
    if find_parents(parent, plan[i]) != find_parents(parent, plan[i+1]):
        result = False

if result:
    print("Yes")
else:
    print("No")
