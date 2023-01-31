#26 카드정렬

# n = int(input())
# cards = [0]*n
# for i in range(n):
#     cards[i] = int(input())

# cards.sort()
# print(cards)

# _sum = cards[0]
# sum_arr = [0]*(len(cards))
# for i in range(1, len(cards)):
#     _sum += cards[i]
#     sum_arr[i] = _sum

# print(sum_arr)

#-----------------------------------
# 처음코드 틀린점 : 처음 sum 이 그 뒤 숫자들보다 작을거라는 보장x.
# sum 도 배열에 넣어서 다시 정렬하고 비교하여 연산해야한다.
#-----------------------------------

#힙 사용

import heapq

n = int(input())

heap = []
for i in range(n):
    heapq.heappush(heap, int(input()))

result = 0

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)

    sum_value = one+two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)