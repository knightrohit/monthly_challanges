"""
Time Complexity = O(N log N)
Space Complexity = O(N)
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals or len(intervals) == 1:
            return intervals
        
        out = []
        intervals.sort()
        start, end = intervals[0]
        for indx, val in enumerate(intervals[1:], 1):
            if end >= val[0]:
                end = max(*val, end)
                continue
            out.append([start, end])
            start, end = val            
        out.append([start, end])
            
        return out