"""
Time/Space Complexity = O(K**2)
"""
# Dynamic Programming
# Bottom Up Approach
from functools import lru_cache

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        out = [1]
        
        if rowIndex == 0:
            return out
        
        @lru_cache(None)
        def search(row, col):
            if row == col or col == 0:
                return 1
            return search(row - 1, col - 1) + search(row - 1, col)

        for i in range(1, rowIndex):
            out.append(search(rowIndex, i))
        
        out.append(1)
        
        return out