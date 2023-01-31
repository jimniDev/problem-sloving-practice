https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2 or n==3:
            return n-1
        res=1
        while n>4:
            n = n-3
            res = res*3
        return n*res
            
#     def integerBreak(self, n: int) -> int:
#         if n == 2:
#             return 1
#         elif n == 3:
#             return 2
        
#         dp = [0] * (n + 1)
        
#         dp[1] = 1
#         dp[2] = 1
#         dp[3] = 2
        
#         for i in range(4, n + 1):
#             l = 1
#             r = i -1
#             p = 0
            
#             while l <= r:
#                 p = max(p, max(l, dp[l]) * max(r, dp[r]))
#                 l += 1
#                 r -= 1