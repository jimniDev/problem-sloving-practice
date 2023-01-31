import sys

def abstract(r, c, l):
    global n, A, res
    start_color = A[r][c]
    divide_flag = False
    
    if l != 1:
        for i in range(l):
            for j in range(l):
                if A[r+i][c+j] != start_color:
                    divide_flag = True
                    break

    if divide_flag:
        res.append('(')
        nl = l//2
        abstract(r, c, nl) #1 up_left
        abstract(r, c +nl, nl) #2 up_right
        abstract(r + nl, c, nl) #3 down_left
        abstract(r+nl, c+nl, nl) #4 down_right
        res.append(')')
    else: 
        res.append(str(start_color))
        
        

def main():
    global n, A, res
    read = sys.stdin.readline

    n = int(input())
    A = [list(map(int, read().rstrip())) for _ in range(n)]
    #흰0 검1
    res = []
    #12
    #34 이렇게 묶어서괄호로표현
    abstract(0, 0, n)
    ans = ''.join(res)
    print(ans)

main()