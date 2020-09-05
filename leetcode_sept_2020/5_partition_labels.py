"""
Time Complexity = O(N)
Space Complexity = O(1)
"""

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        if not S:
            return []
        
        last_indx = {ch:indx for indx, ch in enumerate(S)}
        
        out = []
        i = prev = 0

        for indx, ch in enumerate(S):
            i = max(i, last_indx[ch])
            if i == indx:
                out.append(i + 1 - prev)
                prev = i + 1

        return out