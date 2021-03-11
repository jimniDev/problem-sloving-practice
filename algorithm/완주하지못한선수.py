#완주하지못한선수.py

#1차풀이 - 효율성 빵점이야

# def solution(participant, completion):
#     answer = ''
#     for c in completion:
#         if c in participant:
#             participant.remove(c)
#     return participant[0]

#답 - Collections 모듈 사용
# Counter key,value

import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]