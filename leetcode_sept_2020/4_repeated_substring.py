class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        if not s or len(s) == 1:
            return False

        # solution one
        n = len(s)
        for i in range(1, n//2 + 1):
            if n % i == 0 and n//i * s[:i] == s:
                return True
        return False

# solution two
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        if not s or len(s) == 1:
            return False    

        return s in (s + s)[1:-1]