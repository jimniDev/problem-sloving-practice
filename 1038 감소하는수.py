from itertools import combinations

n = int(input())
ans = []
#1~10자리, 0~9 조합 
for i in range(1, 11):
    for num in combinations(list(range(10)), i):
        desc_arr = sorted(num, reverse=True)
        ans.append(int(''.join(map(str, desc_arr))))

ans.sort()
# print(ans)
if n > len(ans)-1:
    print(-1)
else:
    print(ans[n])
