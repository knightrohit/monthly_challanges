"""
Time complexity = O(N)
Space Complexity = O(1)
"""
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        out = []
        
        for num in nums:
            if nums[abs(num) - 1] < 0:
                out.append(abs(num))
                
            else:
                nums[abs(num) - 1] *= -1
                
        return out