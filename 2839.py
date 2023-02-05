n = int(input())

#3키로, 5키로  -> 몇봉지인지 출력
#정확히 N키로 못맞추면 -1
def delivery(n):
    cnt = 0
    while n >= 3:
        if n % 3 == 0 and n%5 != 0 :
            cnt += s
            n -= 3
        else:
            cnt += 1
            n -= 5
    if n != 0:
        return -1
    return cnt
print(delivery(n))


