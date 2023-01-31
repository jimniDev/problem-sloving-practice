#03 문자열 뒤집기
# 0과1 문자열S, 전부같게, 뒤집기 최소횟수
# 101011 111011 11111 2번
# 101011 110111 11111 2번
# 0101101 0010010 0001100 0000000 3번
# 시작숫자 기준으로 하면 최소횟수되는듯
# 시작숫자랑 다른숫자만나면~ 연속된것 다 뒤집기?
# 합이 len 이거나 0 이면 완료, 그때까지 바꾸기?

# 파이썬 원소 int로
# list_a = list(map(int, list_a))
# list_a = [int (i) for i in list_a]

s = list(map(int, list(input())))
start = s[0]
count = 0
before = start
for i in range(1, len(s)):
    if sum(s) != 0 and sum(s) != len(s):
        num = s[i]
        if num != start:
            s[i] = start
            if num != before:
                count += 1
        before = num
print(count)

#40분 T-T

#답
#전부0,전부1 둘다해봐서 적은횟수로
data = input()
count0 = 0
count1 = 0

#첫번쨰원소
if data[0] == '1':
    count0 += 1
else:
    count1 += 1
#두번째 원소부터
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1': #다음수에서 1로 바뀌는경우
            count0 += 1    
        else: #다음수에서 0으로 바뀌는경우
            count0 += 1
print(min(count0,count1))
