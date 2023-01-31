#02 곱하기혹은더하기

#아이디어1
#곱하기가 손해인경우? 0이 있을때
#0을확인해서 있으면 더하기, 없으면 곱하기

#02984

# a = list(input())
# result = 0
# for i in range(len(a)):
#     if (int(a[i]) != 0):
#         if (int(a[i-1]) != 0):
#             result = result*int(a[i])
#         else:
#             result += int(a[i])
# print(result)

#30분 - 틀림

#아이디어2 - 답안
#두수중 하나라도 1 이하인 경우 더하고, 두수모두 2 이상인경우 곱하기
#result가 1이하거나, 처리하는 숫자가 1이하면 더하기, 아니라면 곱하기
# *내가놓친것 : 두수중하나라도 1인 경우에도 더하기가 낫다

data = input()
result = int(data[0])
for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1 :
        result += num
    else:
        result *= num
print(result)
