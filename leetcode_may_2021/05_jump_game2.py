"""
Time/Space complexity : O(N)
"""

from functools import lru_cache

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def min_jump(indx):

            if indx == len(nums) - 1:
                return 0
            
            if indx >= len(nums) or nums[indx] == 0:
                return float('inf')

            return min(1 + min_jump(indx + i) for i in range(1, nums[indx]+1))        
        
        return min_jump(0)