#25실패율

# 실패율 = 도달햇지만 언클리어/도달
# 스테이지 N, 사용자의멈춘스테이지배열(1~N+1), 실패율 내림차순

# 기수정렬?
# stage크기 fail -> 사용자배열 돌면서 해당 인덱스에 +1
# 실패율 저장 -> rate[i] = (스테이지번호, fail[i]/도전)
# 정렬 (-x[1], x[0]) 으로 정렬

N = int(input())
stages = list(map(int, input().split()))
fail = [0]*N

for i in stages:
    if i <= N:
        fail[i-1] += 1
#print(fail)
rates = []
for i in range(N):
        if (len(stages) - sum(fail[:i]) == 0): #분모가 0일때
            rates.append((i+1, 0))
        else:
            rates.append((i+1, fail[i]/(len(stages) - sum(fail[:i]))))
    rates.sort(key=lambda x: (-x[1], x[0]))
#print(rates)
for rate in rates:
    print(rate[0])
