#1092 배.py

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

time = 0
checked = [0 for _ in range(m)]
count  = 0

position = [0]*n

if max(boxes) > max(cranes):
    print(-1)
else:
    while count < len(boxes):
        for i in range(n): #크레인
            while position[i] < len(boxes):
                #아직 안옮긴 박스 중에서, 옮길수있는 박스를 만날때까지 반복
                if not checked[position[i]] and cranes[i] >= boxes[position[i]]:
                    checked[position[i]] = True
                    position[i] += 1
                    count += 1
                    break
                position[i] += 1
        time += 1
    print(time)
            

