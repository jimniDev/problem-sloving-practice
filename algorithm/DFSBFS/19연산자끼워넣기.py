#19연산자끼워넣기.py

N = int(input())
numbers = list(map(int, input().split()))
# opr = ['+', '-', 'x', '%']
add, sub, mul, div = map(int, input().split())
# 0: +, 1: -, 2: x, 3: % 

min_, max_ = 1e9, -1e9

def dfs(i, res, add, sub, mul, div):
    global min_, max_
    if i == N:
        min_ = min(min_, res)
        max_ = max(max_, res)
    else:
        if add:
            dfs(i+1, res + numbers[i], add-1, sub, mul, div)
        if sub:
            dfs(i+1, res - numbers[i], add, sub-1, mul, div)
        if mul:
            dfs(i+1, res * numbers[i], add, sub, mul-1, div)
        if div:
            dfs(i+1, int(res / numbers[i]), add, sub, mul, div-1)

dfs(1, numbers[0], add, sub, mul, div)
print(max_)
print(min_)

