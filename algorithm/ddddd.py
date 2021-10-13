#ABC
#BCA



def link(str, i, linked, cnt, org):
    # print(linked)
    # print(cnt, str)
    if linked[i] != -1:
        cur = str[i]
        str[i] = org
        idx = linked[i]
        linked[i] = -1
        return link(str, linked[idx], linked, cnt+1, org)
    return cnt+1

linked = [-1,0,1]
str = ["T","B","C"]

cnt = 1
cnt = link(str, linked[0], linked, cnt, 'A')
print(cnt)
        