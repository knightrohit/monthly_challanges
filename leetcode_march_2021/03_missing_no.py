"""
Time/Space complexity = O(N)
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:        
        return next(iter(set(range(len(nums)+1)) - set(nums)))


# Method - 2
"""
Time Complexity = O(N)
Space Complexity = O(1)
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        missing = len(nums)
        
        for i, val in enumerate(nums):
            missing ^= (i ^ val)
            
        return missing