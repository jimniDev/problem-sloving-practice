#눕치킨.py

#단골 상언 : 쿠폰으로 시켜도 쿠폰+1
#비단골 두영: 쿠폰으로 시키면 쿠폰x

#P, M, F, C

import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    P, M , F, C = map(int, input().split())
    chicken = M//P
    current_coupon = (M//P)*C
    non_vip = chicken + (M//P)*C//F
    vip = M//P

    while(current_coupon >= F):
        vip += current_coupon // F
        current_coupon -= (current_coupon // F)*(F-C)
    print(vip - non_vip)



