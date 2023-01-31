s = input()
answer = len(s)
for i in range(1, len(s)//2+1): # 몇개단위로 1 ~ len//2
    result = ''
    count = 1
    letter = s[0:i]
    for j in range(i, len(s)+1, i): # 문자열훑는용
        if letter == s[j:j+i]: #같으면
            count += 1
        else: #이전문자와 다르다면
            if count >= 2:
                result += str(count) + letter
            else:
                result += letter
            letter = s[j:j+i]
            count = 1
    #나머지 문자들 처리
    if count >= 2:
        result += str(count) + letter
    else:
        result += letter
    answer = min(answer, len(result))
print(answer)