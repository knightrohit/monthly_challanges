"""
Time Complexity = O(N)
Space Complexity = O(1)
"""
from itertools import groupby

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        if not seats:
            return 0
        
        dist = seats.index(1)
        seats.reverse()
        dist = max(dist, seats.index(1))
        
        for key, g in groupby(seats):
            if not key:
                size = len(list(g))
                dist = max(dist, (size + 1)//2)
        
        return dist