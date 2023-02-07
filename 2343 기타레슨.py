import sys
read = sys.stdin.readline

n, m = map(int, read().split())
classes = list(map(int, read().split()))

l = max(classes)
r = sum(classes)
blueray_len = 0
while l <= r:
    mid = (l+r)//2
    # print(l,r,mid)
    cur = mid
    cnt = 1
    for i in range(n):
        if cur < classes[i]: #남은가용길이보다 현재원소가 큼 
            cnt += 1
            cur = mid
        cur -= classes[i]
    
    # print(mid, cnt)
    if cnt > m: # 개수가 넘어간다면
        l = mid + 1
    else: #정답 (최소) or 부족하다면
        blueray_len = mid
        r = mid -1

print(blueray_len)