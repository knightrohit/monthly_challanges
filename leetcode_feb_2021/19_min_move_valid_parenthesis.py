"""
Time/Space Complexity = O(N)
"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        braces = []
        s = list(s)
        
        if not s:
            return s
        
        for indx, i in enumerate(s):
            if i == '(':
                braces.append(indx)
            elif i == ')':
                if braces:
                    braces.pop()
                else:
                    s[indx] = ''
                    
        while braces:
            s[braces.pop()] = ''
        
        return ''.join(s)