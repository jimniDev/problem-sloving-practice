import sys
read = sys.stdin.readline

n = int(input())
arr = list(map(int, read().split()))
x = int(input())

arr.sort()
if len(arr) == 1:
    print(0)
else:
    left = 0
    right = len(arr)-1
    ans = 0
    while left < right: #left==right 일때 포함하면 3+3=6 이런게 카운팅되버림 
        cur = arr[left]+arr[right] 
        if cur == x:
            ans += 1
            left += 1
            right -=1
        elif cur < x:
            left += 1
        else:
            right -=1
    print(ans)



