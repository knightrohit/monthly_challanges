"""
Time/Space complexity = O(N)
"""
from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        @lru_cache(maxsize=None)
        def dfs(val = 0, indx = 0):
            
            if indx >= len(nums):
                return val
            
            left, right = indx + 2, indx + 3         
            return max(dfs(val + nums[indx], left), dfs(val + nums[indx], right))
        
        return max(dfs(0,0), dfs(0,1))