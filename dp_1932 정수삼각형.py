n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]

if n == 1:
    print(tri[0])
else:
    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                upleft = 0
            else:
                upleft = tri[i-1][j-1]
            if j == i:
                up = 0
            else:
                up = tri[i-1][j]
            tri[i][j] += max(up, upleft)
    
print(max(tri[n-1]))
        