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


# Approach 2
class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) == 1:
            return False
        
        stack = []
        
        for i in s:
            for p1, p2 in zip([')', ']', '}'], ['(', '[', '{']):
                if i == p1 and stack and stack[-1] == p2:
                    stack.pop()
                    break
            else:
                stack.append(i)
                
        return not stack