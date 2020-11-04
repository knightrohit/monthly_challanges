"""
Time/Space Complexity = O(N)
"""

from itertools import groupby

class Solution:
    def maxPower(self, s: str) -> int:       
        size = 0        
        for i, k in groupby(s):
            size = max(size, len(list(k)))
            
        return size