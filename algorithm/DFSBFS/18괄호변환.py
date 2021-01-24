
def solution(p):
    answer = ''
    #1
    if not p:
         return ''
    #2
    u, v = divide(p)
    #3
    if isRight(u):
        return u + solution(v)
    #4
    else:
        answer += '(' #4-1
        answer += solution(v) #4-2
        answer += ')' #4-3
        #4-4
        u = u[1:len(u)-1]
        for i in u:
            if i == '(':
                answer += ')'
            else:
                answer += '('       
        #4-5
    return answer

def isRight(u):
    stack = []
    
    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
            
    return True
    

def divide(w):
    left = 0
    right = 0
    for i in range(len(w)):
        if w[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return w[:i+1], w[i+1:]
        