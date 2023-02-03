def cut(x, y, size, paper):
    global n, A
    init_val = A[x][y] 
    cut_flag = False
    for r in range(size):
        for c in range(size):
            if A[x+r][y+c] != init_val:
                cut_flag = True
                break
    if cut_flag:
        #짜름
        size = size//3
        for i in range(3):
            for j in range(3):
                cut(x + i*size, y + j*size, size, paper)
    else:
        if init_val == -1:
            paper[0] += 1
        elif init_val == 0:
            paper[1] += 1
        else:
            paper[2] += 1


def main():
    global n, A
    n = int(input())
    A = [list(map(int, input().split())) for _ in range(n)]
    paper = [0,0,0] #-1,0,1
    cut(0, 0, n, paper)
    for i in paper:
        print(i)

main()
