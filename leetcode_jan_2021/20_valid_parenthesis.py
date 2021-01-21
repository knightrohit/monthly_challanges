"""
Time/Space Complexity = O(N)
"""
class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) == 1:
            return False
        
        stack = [s[0]]
        
        for i in s[1:]:
            if i == ')' and stack and stack[-1] == '(':
                stack.pop()

            elif i == ']' and stack and stack[-1] == '[':
                stack.pop()
                
            elif i == '}' and stack and stack[-1] == '{':
                stack.pop()
                
            else:
                stack.append(i)
                
        return not stack