# 시간 초과
# def z_visit(r, c, size, idx):
#     global A,N
    
#     if size > 1:  #2**(n-1) 로 4등분 한 후 재귀방문
#         idx = z_visit(r, c, size-1, idx)
#         idx = z_visit(r, c + 2**(size-1), size-1, idx)
#         idx = z_visit(r + 2**(size-1), c, size-1, idx)
#         idx = z_visit(r + 2**(size-1), c + 2**(size-1), size-1, idx)
#     else:
#         #size == 1. 이라서 2x2짜리임
#         for i in range(2):
#             for j in range(2):
#                 A[r+i][c+j] = idx
#                 idx += 1
#     return idx


def z_visit(r, c, size, idx, dir):
    # print(2**size, r,c, idx, dir)
    if size > 1: #사분면 찾아서 진입
        half = size-1
        #1사분면
        if r <= R < r+ 2**half and c <= C < c+ 2**half:     
            z_visit(r, c, half, idx, 0)
        #2사분면    
        elif r <= R < r+2**half and c+2**half <= C < c+2**size:            
            z_visit(r, c+2**half, half, idx+(2**(2*half)), 1)
       #3사분면
        elif r+2**half <= R < r+2**size and c <= C < c+2**half:     
            z_visit(r+2**half, c, half, idx+(2**(2*half))*2, 2)
        #4사분면
        else:
            z_visit(r+2**half, c+2**half, half, idx+(2**(2*half))*3, 3)      
    else: 
        # size = 1
        # 2x2 사이즈에서 인덱스 찾기
        if r == R and c == C:
            print(idx)
            return 
        elif r == R and c+1 == C:
            print(idx+1)
            return 
        elif r+1 == R and c == C:
            print(idx+2)
            return 
        elif r+1 == R and c+1 == C:
            print(idx+3)
            return 


def main():
    global N,R,C
    N,R,C = map(int, input().split())
    #N을 줬을때 r행 c열은몇번째로 방문하는지
    
    z_visit(0, 0, N, 0, -1)

main()
