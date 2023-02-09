import sys
read = sys.stdin.readline

n = int(input())
A = list(map(int, read().split()))
O = [-1 for _ in range(n)]
stack = []

stack.append(A[-1])

for i in range(-2, -n-1, -1):   
    while stack:
        if stack[-1] > A[i]: #나보다 크면 O큰수
            O[i] = stack[-1] 
            break
        #나보다 작으면 pop
        stack.pop()
        
    stack.append(A[i])
for i in O:
    print(i, end =" ")