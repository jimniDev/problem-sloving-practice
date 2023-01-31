def solution(board, moves):
    answer = 0
    n = len(board)
    basket = []
    for idx in moves:
        for j in range(n):
            if board[j][idx-1] > 0:
                basket.append(board[j][idx-1])
                board[j][idx-1] = 0
                break 
        if len(basket)>1 and basket[-1] == basket[-2]:
            basket.pop()
            basket.pop()
            answer+=2
    print(basket)
    return answer