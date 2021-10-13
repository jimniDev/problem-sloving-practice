import sys
input = sys.stdin.readline
line = 1
while True:
    input_img = str(input().rstrip())
    if input_img == 'END':
        break
    black_cnt = input_img.count('*')
    white = list(input_img.split('*'))
    white = white[1:len(white) - 1]
    if len(white) != black_cnt-1:
        print(line, 'NOT EVEN')
        line += 1
    else:
        white_cnt = 0
        for w in white:
            if len(w) == len(white[0]):
                white_cnt += 1
            else:
                print(line, 'NOT EVEN')
                break;
        if white_cnt == black_cnt-1:
            print(line, 'EVEN')
    line += 1

