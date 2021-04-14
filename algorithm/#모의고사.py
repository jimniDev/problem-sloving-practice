#모의고사.py

def solution(answers):
    answer = []
    n = len(answers)
    giveup = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
   
    correct = [0]*len(giveup)

    for i in range(3): #수포자 만큼
        p = len(giveup[i])
        for j in range(n // p) : #몫만큼
            for l in range(p): #패턴길이만큼  
                print(i, j*p+l, giveup[i][l], answers[j*p+l])
                if giveup[i][l] == answers[j*p+l]: correct[i] += 1
            if j == n//p-1:
                for k in range(n % p):
                    #print(i, j + n-(n%p))
                    print(i, j*p+l+1+k, giveup[i][k], answers[j*p+l+1+k])
                    if giveup[i][k] == answers[j*p+l+1+k]: correct[i] += 1
    print(correct)
    for i in range(3):
        if correct[i] >= max(correct): answer.append(i)
    return answer

#answers = [1,2,3,4,5,6,7,8,9,10,11,12]
answers = [1,2,3,4,5,1,2,3,4,5]
solution(answers)