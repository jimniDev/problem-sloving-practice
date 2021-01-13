#K1KA5CB7

# isaplha() : 숫자및공백있으면 False
# isdigit() : 문자혼용 False
# isalnum() : 알파벳,숫자로만 되어있으면 True

#파이썬 리스트 삭제 del 리스트[인덱스], 리스트.remove(값)
#원소 마지막 추가 append
#리스트.index(입력할index, 값)

#del 하면 반복문시 범위벗어남. str을 만드는식으로

S = list(input())
S.sort()
digitSum = 0
S2 = ''

for i in range(len(S)):
    if (S[i].isdigit() == True):
        digitSum += int(S[i])
    else:
        S2 += S[i]
S2 += str(digitSum)
print(S2)