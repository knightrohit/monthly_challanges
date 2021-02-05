"""
Time/Space Complexity = O(N)
"""

from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        if not nums or len(nums) == 1:
            return 0
        
        no_dict = Counter(nums) 
        
        return max((no_dict[val] + no_dict[val+1] for val in no_dict if val + 1 in no_dict), default = 0)