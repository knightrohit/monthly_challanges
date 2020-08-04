"""
Time complexity = O(N)
Space complexity = O(1)
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if not s or len(s) < 2:
            return True
        
        start, end = 0, len(s) - 1
        out = True

        while start < end:
            if not s[start].isalnum():
                start += 1
                continue
            
            if not s[end].isalnum():
                end -= 1
                continue
                
            if s[start].lower() == s[end].lower():
                start += 1
                end -= 1
                
            else:
                out = False
                break
            
        return out