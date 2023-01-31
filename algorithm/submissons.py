https://leetcode.com/problems/subsets/submissions/

class Solution:
    from itertools import combinations
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums)+1):
            if i == 0:
                result.append([])
            if i == 1:
                for num in nums:
                    result.append([num])
            if i > 1 :
                result += list(combinations(nums, i))
        return result