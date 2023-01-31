# course 원소 숫자 길이 문자열 중 >> 가장 많이 겹친 문자열
# 그 길이만큼 조합 >> Counter로 세서
# (주문한적없거나, 1명) 아니면 answer 에 join  

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order), c)
            temp += combi
        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) != 1:
            for i in counter :
                if counter[i] == max(counter.values()) :
                    answer.append(''.join(i))
    return sorted(answer)