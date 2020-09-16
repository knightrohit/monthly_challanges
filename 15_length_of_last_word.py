"""
Time/Space Complexity = O(N)
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
  
        return len(s.split()[-1]) if s.strip() else 0