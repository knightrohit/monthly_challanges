"""
Time Complexity = O(NlogN)
Space Complexity = O(1)
"""

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        if not intervals:
            return True
        
        intervals.sort()
        prev = intervals[0][1]
        for s, e in intervals[1:]:               
            if s < prev:
                return False            
            prev = e
            
        return True