#3584 가장가까운공통조상

T = int(input())

def find_parent(parent, x):
    if parent[x] != x:
        x = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(T):
    N = int(input())

    parent = [0]*(N+1)

    for i in range(1,N):
        p, c = map(int, input().split())
        parent[c] = p

    a, b = map(int, input().split())
    a_parent = [a]
    b_parent = [b]

    while parent[a]:
        a_parent.append(parent[a])
        a = parent[a]
    while parent[b]:
        b_parent.append(parent[b])
        b = parent[b]

    a_level = len(a_parent)-1
    b_level = len(b_parent)-1

    while a_parent[a_level] == b_parent[b_level]:
        a_level -= 1
        b_level -= 1
    print(a_parent[a_level +1])
    
