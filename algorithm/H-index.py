#H-index.py

import bisect

def solution(citations):
    citations.sort()
    n = len(citations)
    curr = 0
    for i in range(0, citations[-1]+1):
        idx = bisect.bisect_left(citations, i, 0, n)
        if i <= n-idx and curr <= i:
            curr = max(i, curr)
    return curr

def solution(citations):
    citations.sort()
    n = len(citations)
    curr = 0
    for i in range(0, citations[-1]+1):
        if citations[i] >= n-i:
            return n-i
    return 0