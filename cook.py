
T = int(input())

def combinations(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:], r-1):
                yield [arr[i]] + next

for test_case in range(1, T + 1):
    N = int(input())
    food = list(x for x in range(N))
    S = [list(map(int, input().split())) for _ in range(N)]
    # print(food)
    A_comb = list(combinations(food, N / 2))
    diff = int(1e9)
    for i in range(len(A_comb)//2):
        A = A_comb[i]
        B = list(set(food) - set(A_comb[i]))
        A_S, B_S = 0, 0
        for a in combinations(A, 2):
            A_S += (S[a[0]][a[1]] + S[a[1]][a[0]])
        for b in combinations(B, 2):
            B_S += (S[b[0]][b[1]] + S[b[1]][b[0]])
        # print(A_S, B_S)
        diff = min(abs(A_S - B_S), diff)
    print('#{} {}'.format(test_case, diff))




