#고정점찾기
import sys
import time

start = time.time() 

n = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

# n = 5
# arr = [-15, -6, 1, 3, 7]

def binary(arr, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            start = mid + 1
        else:
            end = mid-1
    return None

result = binary(arr, 0, n-1)
if result == None:
    print(-1)
else:
    print(result)

print("time :", time.time() - start)