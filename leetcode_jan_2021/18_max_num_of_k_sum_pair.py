"""
Time Complexity = O(N^2)
Space Complexity = O(1)
"""
#TLE
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        if len(nums) == 1:
            return 0
        
        operation = 0
        
        for i, v1 in enumerate(nums):
            if v1 != 0:
                for j, v2 in enumerate(nums[i+1:], i+1):                
                    if v2 != 0 and v1 + v2 == k:
                        operation += 1
                        nums[i] = nums[j] = 0
                        break
                    
        return operation


#Approach - 2
"""
Time/Space Complexity = O(N)
""" 
from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        if len(nums) == 1:
            return 0
        
        operation = 0
        num_dict = Counter(nums)
        
        for no in nums:
            if num_dict[k-no] > 0 and num_dict[no] > 0:
                
                if k - no == no and num_dict[no] < 2:
                    continue                    
                num_dict[k-no] -= 1
                num_dict[no] -= 1                    
                operation += 1

        return operation