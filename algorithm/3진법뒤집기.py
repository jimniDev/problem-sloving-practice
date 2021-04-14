def solution(n):
    ans = 0
    tri = []
    if n>=3:
        while(n>=3):
            tri.append(n%3)
            n //= 3
        tri.append(n)
    else:
        tri.append(n%3)
    for i in range(1, len(tri)+1):
        ans += (3**(i-1))*tri[-i]
    return ans