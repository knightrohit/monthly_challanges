"""
Time/Space Complexity = O(N)
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or not k:
            return nums
        
        k = k % len(nums)
        
        out = [0]*len(nums)
                
        for i, val in enumerate(nums):
            if i + k >= len(nums):
                i = abs(len(nums) - (i+k))
                out[i] = val
            else:
                out[i+k] = val
        
        for i in range(len(out)):
            nums[i] = out[i]