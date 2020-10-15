"""
Time/Space Complexity = O(N)
"""
#TLE
class Solution:
    def rob(self, nums: List[int]) -> int:        
       
        def rob(indx = 0, start = 0):
            
            if indx >= len(nums): 
                return 0
            if start == 0 and indx == len(nums) - 1: 
                return 0
            
            return nums[indx] + max(rob(indx+2, start), rob(indx+3, start))
            
        out = 0
        if len(nums) == 1:
            return nums[0]
        
        elif len(nums) == 3:
            return max(rob(0,0), rob(1,1), rob(2,2))
        elif len(nums) == 2:
            return max(rob(0,0), rob(1,1))
        else:
            return max(rob(i, i) for i in range(len(nums)//2))