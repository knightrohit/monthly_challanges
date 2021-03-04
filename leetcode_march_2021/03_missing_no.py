"""
Time/Space complexity = O(N)
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:        
        return next(iter(set(range(len(nums)+1)) - set(nums)))