n = int(input())
cow = [list(map(int, input().split())) for _ in range(n)]

cow = sorted(cow, key=lambda x: (x[0], x[1]))
cur = sum(cow[0])
for i in range(1, len(cow)):
    if cur > cow[i][0]:
        cur += cow[i][1]
    else:
        cur = cow[i][0] + cow[i][1]
# print(cow)
print(cur)

