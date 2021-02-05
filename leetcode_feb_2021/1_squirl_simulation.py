"""
Time Complexity = O(N)
Space Complexity = O(1)
"""
class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        
        def distance(a, b):
            return abs(a[0]-b[0]) + abs(a[1]-b[1])
        
        dst = 0
        min_d = 0
        for nut in nuts:
            dst += distance(tree, nut)*2
            
            
        return dst + min(distance(squirrel, nut) - distance(tree, nut) for nut in nuts)
            