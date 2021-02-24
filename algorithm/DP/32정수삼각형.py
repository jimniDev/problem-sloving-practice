n = int(input())
tri = []
for i in range(n):
    tri.append(list(map(int, input().split())))

#print(tri)

for i in range(1, n): #두번째줄부터
    for j in range(i+1):     
        if j == 0:
            upleft = 0
        else:
            upleft = tri[i-1][j-1]
        if j == i:
            up = 0
        else:
            up = tri[i-1][j]
        
        tri[i][j] += max(upleft,up)
        
print(max(tri[n-1]))
            
