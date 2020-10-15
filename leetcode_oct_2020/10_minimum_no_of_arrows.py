"""
Time Complexity = O(N)
Space Complexity = O(1)
"""

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        if not points:
            return 0
        
        points.sort()
        
        px1, px2 = points[0]
        count = 1
        
        for x1, x2 in points[1:]:
            if x1 <= px2:
                px1 = max(x1, px1)
                px2 = min(x2, px2)
            else:
                count += 1
                px1 = x1
                px2 = x2

        return count