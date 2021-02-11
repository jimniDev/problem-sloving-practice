#부품찾기
#가게부품 N개, 손님이 찾는 부품 M개

import sys

def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)

n = int(sys.stdin.readline().rstrip())
stores = list(map(int, sys.stdin.readline().rstrip().split()))
stores.sort()
m = int(sys.stdin.readline().rstrip())
customers = list(map(int, sys.stdin.readline().rstrip().split()))

for customer in customers:
    ans = binary_search(stores, customer, 0, n-1)
    if (ans == None):
        print('no')
    else:
        print('yes')



