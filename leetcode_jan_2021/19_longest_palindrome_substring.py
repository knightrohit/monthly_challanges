"""
Time Complexity = O(N^2)
Space Complexity = O(1)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) == 1:
            return s

        result = 0
        result_len = 0
        
        for i in range(len(s)):
            # for odd
            
            l = r = i
            while  l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > result_len:
                    result_len = r - l + 1
                    result = s[l: r + 1]
                l -= 1
                r += 1
                
            
            # for even
            l = i
            r = i + 1
            while  l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > result_len:
                    result_len = r - l + 1
                    result = s[l: r + 1]
                l -= 1
                r += 1
                
        return result