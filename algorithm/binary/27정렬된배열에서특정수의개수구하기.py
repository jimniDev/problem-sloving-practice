#27정렬된배열에서특정수의개수구하기
# N개원소, target x, 몇번등장?

import sys
import time

def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) //2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid+1, end)
    elif arr[mid] == target:
        return binary_search(arr, target, start, mid-1)
        
def binary_left(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) //2
    if arr[mid] == target and arr[mid-1] != target: 
        return mid
    else:
        return binary_search(arr, target, mid+1, end)

def binary_right(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) //2
    if arr[mid] == target and arr[mid+1] != target:
        return mid
    else:
        return binary_search(arr, target, start, mid-1)

start = time.time() 

n, x = map(int, input().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

val = binary_search(arr, x, 0, n-1)
if val == None:
    print(-1)
else:
    target_start = binary_left(arr, x, 0, val-1)
    target_end = binary_right(arr, x, val+1, n-1)
    print(target_end - target_start + 1)

print("time :", time.time() - start)
