n = int(input())
build_frame = input()

build = [[-1]*n]*n

for i in build_frame:
    x,y,a,b = i[0],i[1],i[2],i[3]
    if a == 0 and b == 1: #기둥 설치 
        if y == 0:
            build[x][y]= 0
        else:
            if build[x][y-1] == 0 or build[x-1][y] == 1:
                build[x][y]= 0 
                
    elif a == 0 and b == 0: #기둥 삭제
        if build[x-1][y+1] == 1 and (build[x-1][y] == 0 or build[x][y+1] == 1):
            build[x][y]= -1
        elif build[x][y+1] == 1 and (build[x+1][y] == 0 or build[x+1][y+1] == 1):
            build[x][y]= -1
        elif build[x][y+1] == 0 and (build[x-1][y+1] == 1 or build[x][y+1] == 1):
            build[x][y]= -1 
            
    elif a == 1 and b == 1: # 보 설치
        if y == 0:
            build[x][y]= 1
        else:
            if build[x][y-1] == 0 or build[x-1][y ]== 1:
                build[x][y]= 1                
                
    #elif a == 1 and b == 0: # 보 삭제

print(build)

#자물쇠 90 180 270 코드 만들어놓기