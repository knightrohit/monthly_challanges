from functools import lru_cache

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        row, col = len(triangle), len(triangle[-1])
        
        @lru_cache(None)
        def minVal(r = 0, c = 0):
            
            if r == row - 1:
                return triangle[r][c]                       
            else:
                return triangle[r][c] + min(minVal(r+1, c), minVal(r+1, c+1))            
            
        return minVal()