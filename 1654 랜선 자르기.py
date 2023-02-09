import sys
read = sys.stdin.readline

k, n = map(int, read().split())
lan = list(int(read().rstrip()) for _ in range(k))

l = 1
# r = min(lan) #모든 랜선을 쓸 필요는 없다...... 
# 어차피 logg하면 10억도 두자리 되니까 최~대로 잡기
r = 2**31-1
max_len = 0

while l<=r:
    mid = (l+r)//2
    cur = mid # 현재 시도하는 랜선 길이
    cnt = 0 # 잘라서 총 몇개 나오는지
    for i in range(k):
        if lan[i] >= cur: #남은 길이가 mid 보다 작다면 다음으로 넘어감
            # print(cur, lan[i] // cur)
            cnt += lan[i] // cur

    print(l, r, mid, cnt)
    if cnt < n: #mid를 줄여
        r = mid - 1
    else: #mid를 키워 (최댓값 구하기), n개보다 많이 구해도 n개를 만드는게 됨
        max_len = mid
        l = mid + 1


print(max_len)
            