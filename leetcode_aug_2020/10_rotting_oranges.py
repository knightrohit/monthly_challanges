"""
Time/Space Complexity = O(row*col)
"""
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        row, col = len(grid), len(grid[0])
        fresh_orange = 0
        rooten_orange = deque()        
        
        # Find out total fresh orange
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh_orange += 1
                    
                elif grid[r][c] == 2:
                    rooten_orange.append((r, c, 0))
        minute = 0            
        while rooten_orange:            
            if rooten_orange[0][2] == minute:
                x, y, minute = rooten_orange.popleft()
                
                for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + i, y + j
                    
                    if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_orange -= 1
                        rooten_orange.append((nx, ny, minute + 1))
                        
            else:
                minute += 1
            
        return -1 if fresh_orange > 0 else minute