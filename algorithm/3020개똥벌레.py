#3020개똥벌레.py
import sys

input = sys.stdin.readline
n, h = map(int, input().split())
print(n, h)
top = []
down = []
for i in range(n):
    if i%2 == 0:
        down.append(int(input()))
    else:
        top.append(int(input()))

top.sort()
down.sort()
min_cnt = n
frequency = 0

def binary(arr, target, start, end):
    while (start <= end):
        mid = (start + end)//2
        if target > arr[mid]:
            start = mid+1
        else:
            end = mid-1
    return start

for i in range(1, h+1):
    top_cnt = len(top) - binary(top, h - i +0.5, 0, len(top)-1)
    down_cnt = len(down) - binary(down, i-0.5, 0, len(down)-1)
    print('left', binary(down, i-0.5, 0, len(down)-1))

    if min_cnt > top_cnt + down_cnt:
        min_cnt = top_cnt + down_cnt
        frequency = 1
    elif min_cnt == top_cnt + down_cnt:
        frequency += 1

print(min_cnt, frequency)



