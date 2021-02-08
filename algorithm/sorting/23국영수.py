# 이름 국 영 수
# 1. 국어감소 2.영어증가 3. 수학감소 4.이름사전오름차순

# sort key lambda 사용!!!!

n = int(input())
students = []
for i in range(n):
    students.append(tuple(input().split()))

students.sort(key=lambda x: (((-int(x[1]), int(x[2])), -int(x[3])), x[0]))

for student in students:
    print(student[0])

