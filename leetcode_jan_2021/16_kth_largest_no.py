"""
Time Complexity = O(nlogn)
Space Complexity = O(1)
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        if not nums:
            return nums
        
        return sorted(nums)[-k]