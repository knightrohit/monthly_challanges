"""
Time Complexity = O(NlogN)
Space Complexity = O(1)
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0
        
        prev, out = float('-inf'), 0

        for i, j in sorted(intervals, key = lambda x : x[1]):
        
            if not i >= prev:
                out += 1
                continue
                
            prev = j
            
        return out