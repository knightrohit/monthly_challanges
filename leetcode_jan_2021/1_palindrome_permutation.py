"""
Time Complexity - O(N)
Space Complexity - O(1)
"""
from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        if not s:
            return False
        
        count = Counter(s)
        
        odd = 0
        for val in count.values():
            if val%2:
                odd += 1
            if odd > 1:
                return False
            
        if odd:
            return True if len(s)%2 else False
        else:
            return True if not len(s)%2 else False