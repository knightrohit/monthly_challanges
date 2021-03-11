"""
Time/Space complexity = O(N)
"""
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        swap = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        out = []
        for i in num:
            if i in swap:
                out.append(swap[i])
            else:
                return False
            
        return ''.join(out) == num[::-1]