
# 현재빌딩에서 오른쪽 max 인덱스 - 왼쪽 max 인덱스 = 보이는 빌딩수

# def view_buildings(arr):
#     max_buildings = 0
#     for i in range(1, len(arr)+1):
#         #left

#         max_left = arr[:i+1].index(max(arr[:i+1])) #i포함
#         max_right = arr[i:].index(max(arr[i:])) #i포함
#         print(i,max_left, max_right)
#         # print(i+1, max_buildings, abs(max_right - max_left))
#         max_buildings = max(max_buildings, abs(max_right - max_left))
#     return max_buildings

# N = int(input())
# bulidings = list(map(int, input().split()))
# print(view_buildings(bulidings))

print([1,2,3][:2])
