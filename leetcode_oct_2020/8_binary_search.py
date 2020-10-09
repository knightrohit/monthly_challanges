"""
Time Complexity = O(N)
Space Complexity = O(1)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1
        mid = 0

        while start <= end:
            
            mid = (start + end)//2

            if nums[mid] == target:
                return nums.index(target)
            
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
                
        return -1