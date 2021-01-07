# problem-sloving-practice
PS practice

## 푼 문제
### 입출력
2557, 1000, 2558, 10950, 10951, 10952, 10953, 11021, 11022, 11718, 11719, 11720, 11721, 2741, 2742, 2739, 1924, 8393, 10818, 2438, 2439, 2440, 2441, 2442, 2445, 2522, 2446, 10991, 10992


## Python 정리

map : 리스트의 요소를 지정된 함수로 처리

sep='' 중간
end='' 끝
\n : 다음 줄로 이동(개행)
\r :해당 줄의 처음으로 이동
\t : 8칸 공백
\' : '문자
\" : "문자
\ : \문자

### input()
내장함수취급
사용자의 입력을 받고 → 문자열로 변환 → 추가 strip 진행
더 이상 입력이 없는데도 수행될 경우 EOFerror를 뱉어

### sys
file object 취급, 따로 buffer
sys.stdin.readline() - 한줄을 iterable 한 객체에 저장 (개행포함)
readline(숫자) : 입력받을 만큼 입력받기 가능
더이상 입력 없으면 빈 문자열을 반환
sys.stdin - 여러줄 받으려면

n = input()
a = [sys.stdin.readline() for i in range(n)]

### range(start,stop,step)
- 오름차순일땐 stop-1까지. 내림차순일땐 stop+1까지
  
*args : 여러개 받고자 할 때
**kwags : 함수 키워드

rjust
문자열.rjust(공백포함길이, "공백문자") 

center
String.center(길이, '추가할 문자')
