import sys
read = sys.stdin.readline

N = int(input()) #후보자수
candidates = {can : i for i, can in enumerate(list(read().split()))}
M = int(input()) #투표인원
votes = [list(read().split()) for _ in range(M)] # [이름, 점수]

# print(candidates.items())
result = {name : [0, idx] for name,idx in candidates.items()}

for name, score in votes:
	key = candidates.get(name)
	if key != None:
		result[name][0] += int(score)

result = sorted(result.items(), key= lambda x: (-x[1][0], x[1][0]))
# print(result)

for i in range(3):
	print(result[i][0], result[i][1][0])
