N = int(input())

members = []
for _  in range(N):
    members.append(list(map(int, input().split())))

members = sorted(members,key=lambda x: (x[1], x[0]))

# print(members)

start, end = members[0][0], members[0][1]
cnt = 1

for i in range(1, len(members)):
    cur_s, cur_e = members[i]
    if cur_s >= end:
        start, end = cur_s, cur_e
        cnt += 1
        # print(cnt, cur_s, cur_e)
    
print(cnt)