a, b = map(int, input().split())
#input().split() 결과는 리스트
#map 객채 = <map object at 0x00000256DC840040> 들여다볼수X, 이터레이터

a = list(map(int,a))

#2차원배열
array = [[0]*11 ]*10
for i in array :
    for j in i:
        print(j,end=" ")
    print()

#10951
#어디가 끝인지 알수없으니 EOF까지.
#정석적인 방법을 쓰려면 import sys.
#try except
#EOFError

#풀이1
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except EOFError:
        break
 
# 풀이2
import sys
 
for line in sys.stdin:
    a, b = map(int, line.split())
    print(a + b)

 
# 풀이3
try:
    while 1:
        a,b = map(int, input().split())
        print(a+b)
except:
    exit()

#10952번
while True:
    a, b = map(int, input().split())
    if a == 0 and b==0:
        break
    print(a+b)

#10953번
x = int(input())
for i in range(x):
    a,b = map(int, input().split(','))
    print(a+b)

#11021번
x = int(input())
for i in range(x):
    a,b = map(int, input().split())
    print('Case #%d:' %(i+1), a+b)

#11022번
x = int(input())
for i in range(x):
    a,b = map(int, input().split())
    print('Case #%d: %d + %d =' %(i+1,a,b), a+b)

#11718번
#내풀이
while True:
    try:
        a = input()
        print(a)
    except EOFError:
        break

#더 짧은 풀이
import sys
print(sys.stdin.read()) #readline, lines 와의 차이가 뭐야? 왜 틀려?

#11719
import sys
print(sys.stdin.read())

#11720
x = int(input())
a = list(input())
amount = 0
for i in range(x):
    amount += int(a[i])
print(amount)

#11721
#내풀이
s = list(input())
for i in range((len(s)//10)+1):
    print(''.join(s[10*i:10*(i+1)]))

#다른풀이
a=str(input())
n=0
for i in a:
    print(i,end='')
    n=n+1
    if n==10:
        print()
        n=0

#2741
#내풀이

#더빠른풀이
a = range(1,int(input())+1)
print('\n'.join(map(str,a)))

#더빠른 풀이2
import sys
print('\n'.join(map(str, range(1, int(sys.stdin.readline()) + 1))))i

#2742
#입숫자역순출력
import sys
print('\n'.join(map(str,range(int(sys.stdin.readline()), 0, -1))))

#1924
#요일출력
#내답
a,b = map(int, input().split())
m = [31,28,31,30,31,30,31,31,30,31,30,31]
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
days = 0
for i in range(a-1):
    days += m[i]
print(day[(days+b)%7])

#다른풀이
x, y = map(int, input().split())
for i in range(1, x):
    if i in [1, 3, 5, 7, 8, 10, 12]:
        y += 31
    elif i == 2:
        y += 28
    else:
        y += 30
day_week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
print(day_week[y % 7])

#다른풀이
print(day[(sum(month[0:a])+b)%7])

#8393 - N까지의합
#내풀이
n =int(input())
print(sum(list(range(1,n+1))))
#더빠른풀이
#등차수열의합
n = int(input())
print((n**2+n)//2)

#10818 - 최대최소
#내풀이
n =int(input())
a = list(map(int, input().split()))
print(min(a), max(a))
#다른사람풀이
import sys
a, *b = map(int, sys.stdin.read().split())
print(min(b), max(b))

#2438 별출력
#나
n = int(input())
for i in range(1,n+1):
    print('*'*i)

#2439 우측정렬 별출력
n=int(input())
for i in range(1,n+1):
    print(' '*(n-i)+'*'*i)

#2440 역순 별찍기
n = int(input())
for i in range(n,0,-1):
    print('*'*i)

#2441,2442,2445
n = int(input())
for i in range(n):
   print('*'*(i+1)+' '*2*(n-i-1)+'*'*(i+1))
for i in range(n-2,-1,-1):
   print('*'*(i+1)+' '*2*(n-i-1)+'*'*(i+1))

#2446
n = int(input())
for i in range(n):
    print(' '*i+'*'*(2*(n-i)-1))
for i in range(n-2,-1,-1):
    print(' '*i+'*'*(2*(n-i)-1))

#10991
n = int(input())
for i in range(1,n+1):
    print(' '*(n-i)+'* '*i)

#rjust쓴풀니
n = int(input())
s = '* '*n
for i in range(n):
	print(s[:2*i+1].rjust(n+i, ' '))

#10992
n = int(input())
for i in range(n-1):
    if i==0:
        print(' '*(n-i-1)+'*')
    else:
        print(' '*(n-i-1)+'*'+' '*(2*i-1)+'*')
print('*'*(2*n-1))

#center풀이
n=int(input())
for i in range(n-1):
    print(' '*(n-i-1) + (' '*(2*i-1)).center(2*i+1,'*'))
print('*'*(2*n-1))