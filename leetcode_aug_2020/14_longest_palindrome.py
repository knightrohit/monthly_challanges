"""
Time Complexity = O(N)
Space Complexity = O(1)
"""
from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
       
        ch_dict = Counter(s)
        out = 0

        for val in ch_dict.values():
            
            if val % 2 == 0:
                out += val                
            
            else:
                out += val if not out % 2 else val - 1

        return out


# Using Generator
from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        val = sum(v & 1 for v in Counter(s).values())
        return len(s) - val + bool(val)
