N = list(map(int, input()))
left = 0
right = 0
for i in range(len(N)):
    if i < len(N)//2:
        left += N[i]
    if i >= len(N)//2:
        right += N[i]
#print(left, right)
if left == right:
    print('LUCKY')
else:
    print('READY')
