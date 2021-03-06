#27정렬된배열에서특정수의개수구하기
# N개원소, target x, 몇번등장?

import sys
import time
start = time.time() 

def binary_left(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target and (arr[mid-1] < target or mid == 0): 
        return mid
    elif arr[mid] >= target:
        return binary_left(arr, target, start, mid-1)
    else:
        return binary_left(arr, target, mid+1, end)

def binary_right(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target and (arr[mid+1] > target or mid == n-1):
        return mid
    elif arr[mid] <= target:
        return binary_right(arr, target, mid+1, end)
    else:
        return binary_right(arr, target, start, mid-1)    

n, x = map(int, input().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))


target_start = binary_left(arr, x, 0, n-1)
print(target_start)
if target_start == None:
    print(-1)
else:
    target_end = binary_right(arr, x, target_start, n-1)
    print(target_end - target_start + 1)

print("time :", time.time() - start)
