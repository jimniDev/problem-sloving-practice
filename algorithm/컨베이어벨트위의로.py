import sys
input = sys.stdin.readline

N,K = map(int, input().split())
belt = list(map(int, input().split()))
robot = [0 for _ in range(N)]
stage = 1

def shift(arr,robot):
    tmp = arr[-1]
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]
    for i in range(N-1, 0, -1):
        robot[i] = robot[i-1]
    robot[0] = 0
    arr[0] = tmp
    robot[-1] = 0

while True:
    shift(belt, robot)
    # print(stage, '-1: ', belt)
    # print(robot)
    #가장 먼저 벨트에 올라간 로봇부터 조건 뺴먹음
    for i in range(N-2, -1 , -1):
        if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] >= 1:
            robot[i+1], robot[i] = 1, 0
            belt[i + 1] -= 1
    robot[-1] = 0
    # print(stage, '-2: ', belt)
    # print(robot)
    if robot[0] == 0 and belt[0] > 0:
        robot[0] = 1
        belt[0] -= 1
    # print(stage, '-3: ', belt)
    # print(robot)
    # print('0:', belt.count(0))
    if int(belt.count(0)) >= K:
        break;
    stage += 1

print(stage)
