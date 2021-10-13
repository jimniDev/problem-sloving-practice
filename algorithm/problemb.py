import sys
input = sys.stdin.readline

while True:
    input_img = str(input().rstrip())
    if input_img == 'END':
        break
    black_cnt = input_img.count('*')
    white = list(len(input_img.split('*')))
    white = white[1:len(white)-1]
    # for i in range(black):
    #     white[i]

    print(black_cnt, white)