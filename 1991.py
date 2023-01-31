# import sys
# read = sys.stdin.readline

# n = int(read())
# ppl = sorted([list(map(int, read().split())) + [i] for i in range(n)], reverse=True)
# #x, y, 인덱스, 등수
# rank_arr = [-1 for _ in range(n)]

# max_x, max_y = -1e9, -1e9
# rank = 1
# same = 1

# for i in range(len(ppl)):
#     if i == 0:
#         rank_arr[ppl[i][2]] = rank
#     else:
#         if ppl[i][0] < ppl[i-1][0] and ppl[i][1] < ppl[i-1][1]: #x y 둘다 앞보다 작으면
#             rank += same
#             rank_arr[ppl[i][2]] = rank
#             same = 1
#         else: #글친않으면 앞과 같은 등수
#             rank_arr[ppl[i][2]] = rank
#             same += 1

# for i in rank_arr:
#     print(i, end=" ")


# **구현은.. 문제 조건을 그대로 받아들이는게 피료함. 특히 굳이 조건식을 준 경우

import sys
read = sys.stdin.readline

n = int(read())
ppl = [list(map(int, read().split())) for i in range(n)]

for i in range(len(ppl)):
    cnt = 1
    for j in range(len(ppl)):
        if i != j:
            if ppl[i][0] < ppl[j][0] and ppl[i][1] < ppl[j][1]:
                cnt += 1
    print(cnt, end=" ")
