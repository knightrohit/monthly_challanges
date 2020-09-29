#TLE
from functools import reduce

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        out = 0

        for _ in range(1, len(nums)+1):
            start = 0
            end = _
            while end <= len(nums):
                if end == 1:
                    for _, val in enumerate(nums):
                        if val < k:
                            out += 1
                    break
                else:
                    if reduce(lambda a, b : a*b, nums[start:end]) < k:
                        out += 1
                    
                start += 1
                end += 1
                
        return out


"""
Time Complexity = O(N)
Space Complexity = O(1)
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if not nums or k <= 1:
            return 0
        
        start = 0
        prod = 1
        count = 0
        
        for end, val in enumerate(nums):
            
            prod *= val
            
            while prod >= k:
                prod /= nums[start]
                start += 1
                
            count += end - start + 1
            
        return count