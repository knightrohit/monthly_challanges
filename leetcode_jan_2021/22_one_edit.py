"""
Time Complexity = O(N)
Space Complexity = O(1)
"""

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        
        # only one character should be different
        p1 = 0
        p2 = 0
        diff = 0
        if (s and len(s) == 1 and not t) or (t and len(t) == 1 and not s):
            return True
        
        
        if len(s) == len(t):
            while p1 < len(s):
                if s[p1] != t[p1]:
                    diff += 1
                p1 +=1

        # Delete from s
        elif len(s) - 1 == len(t):
            while p1 < len(s) and p2 < len(t):
                if s[p1] != t[p2]:
                    diff += 1
                    p1 += 1
                    continue
                p1 += 1
                p2 += 1
                    
            if p1 < len(s):
                diff += 1

        # Add an element in s
        elif len(s) + 1 == len(t):
            while p1 < len(s) and p2 < len(t):
                if s[p1] != t[p2]:
                    diff += 1
                    p2 += 1
                    continue                    
                p1 += 1
                p2 += 1
                
            if p2 < len(t):
                diff += 1

                
        return diff == 1