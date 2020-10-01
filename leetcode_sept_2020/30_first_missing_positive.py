"""
Time Complexity = O(nlogn)
Space Complexity = O(1)
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        if not nums:
            return 1

        # Replacing unwanted value
        for indx, val in enumerate(nums):
            if val <= 0:
                nums[indx] = float('inf')
           
        # Sort the value
        nums.sort()
        
        if nums[0] > 1 or nums[0] == 0:
            return 1
        
        prev = nums[0]
        
        for i in nums[1:]:
            if i - prev > 1:
                return prev + 1
            prev = i

        return nums[-1] + 1