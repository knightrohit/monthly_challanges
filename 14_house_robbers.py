"""
Time/Space complexity = O(N)
"""
# Top Down Approach
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


# Bottom UP
from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        hr = [0]*len(nums)
        
        for i, v in enumerate(nums):
            hr[i] = max((hr[i-2] if i - 2 >= 0 else 0) + v, hr[i-1] if i - 1 >= 0 else 0)            
        return hr[-1]
            