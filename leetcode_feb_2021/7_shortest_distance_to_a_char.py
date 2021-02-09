"""
Time/Space Complexity = O(N)
"""

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        
        if not s or not e:
            return []
        
        out = []
        ch_indices = [indx for indx, char in enumerate(s) if char == c]
        
        if not ch_indices:
            return []
        
        size = len(s)
        i = 0
        p1 = float('inf')
        p2 = ch_indices[i]
        
        for j in range(len(s)):
            val = min( abs(p1-j), abs(p2-j))
            out.append(val)
            if j == p2:
                p1 = p2
                p2 = ch_indices[i+1] if i+1 < len(ch_indices) else p2
                i += 1
                
        return out