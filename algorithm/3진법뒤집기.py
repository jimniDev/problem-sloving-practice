def solution(n):
    ans = 0
    tri = []
    while(n>0):
        tri.append(n%3)
        n //= 3
    for i in range(1, len(tri)+1):
        ans += (3**(i-1))*tri[-i]
    return ans

def solution(n):
    ans = 0
    tri = ''
    while(n>0):
        tri += str(n%3)
        n //= 3
    ans = int(tri,3)
    return ans