# 2,3,5만을 소인수로 가지는수 
# 1은 못생긴수
# 1 2 3 4 5 6 7 8 9 10 12 15 ...
# n번쨰 못생긴수 출력

# i%2 != 0 i%3 != 0 i%5 != 0 이면 탈락
# u 배열 제외한 수로 나눠지면 탈락 = u 배열 안에 있는 수로만 나눠져야됨
# ai = i를 약수로 가지는 최대 합성수
# a2, a3, a5

# 안못생긴 수를 담아두고 그걸로 나눠지면 빼야되는거 아니야?
# pretty = (7, 11, 13, 14, ...
# 7, 11, 13, 17, 19 ..

# 2 3 5, 4 6 10, 
# 2, 3, 5 의 배수를 차례로 고려


n = int(input())
ugly = [0]*(n+1) #dp 배열

ugly[1] = 1
pretty = []
prev = 1
for i in range(2, n):
    if i%2 != 0 and i%3 != 0 and i%5 != 0:
        pretty.append(i)
    
    
    


print(ugly)