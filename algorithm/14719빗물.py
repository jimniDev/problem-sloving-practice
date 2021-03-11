#14719빗물.py

# 4 4
# 3 0 1 4

# 4 8
# 3 1 2 3 4 1 1 2

h, w = map(int, input().split())
arr = list(map(int, input().split()))
# wall = []
# spaces = 0
# result = 0

# for i in range(w):
#     #첫 벽
#     if len(wall) == 0 and arr[i] > 0:
#         wall = i, arr[i]
#         print(wall)
#     else:
#         # 벽 생기고부터
#         if len(wall) > 0:
#             if wall[1] > arr[i]: #고임
#                 spaces += 1
#             elif wall[1] <= arr[i]: # wall 갱신
#                 if spaces > 0:
#                     for space in range(1, spaces+1):
#                         result += min(wall[1], arr[i]) - arr[i-space]
#                 wall = i, arr[i]
#                 print(wall)
#                 spaces = 0

# print(result)

#현재인덱스에서 min(왼쪽 max, 오른쪽max) - 현재높이

def trapping_rain(arr):
    raindrop = 0
    for i in range(len(arr)):
        max_left = max(arr[:i+1]) #i포함
        max_right = max(arr[i:]) #i포함
        raindrop += min(max_left, max_right) - arr[i]
    return raindrop

print(trapping_rain(arr))
    

