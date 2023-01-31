import sys
global n, paper, blue, white

def check_color(r, c, l):
    # 시작 좌표 r,c 길이 l
    global n, paper, blue, white
    start_color = paper[r][c]
    nl = l//2
    cut = False
    if l != 1:
        for i in range(l):
            for j in range(l):
                if paper[r+i][c+j] != start_color:
                    #같지않음 잘라야됨
                    cut = True
                    break

    if cut:
        # print("잘라야됨", r,c,l)
        check_color(r, c, nl)
        check_color(r+nl, c, nl)   
        check_color(r, c+nl, nl)
        check_color(r+nl, c+nl, nl)        
    else:            
        #무사히통과. 안잘라도됨
        if start_color:
            blue +=1
        else:
            white +=1

def main():
    global n, paper, blue, white
    read = sys.stdin.readline

    #N은 2, 4, 8, 16, 32, 64, 128 중 하나
    n= int(input())
    paper = [list(map(int, read().split())) for _ in range(n)]
    #파랑1  하얀0

    #sum 체크해서 all 1 or all 0아니면 자름
    # 만약 n==1 이거나 all 만족하면 blue+ or white+
    blue = 0
    white = 0 

    check_color(0,0,n)

    print(white)
    print(blue)


main()