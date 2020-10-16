"""
Time Complexity = O(NlogN)
Space Complexity = O(N)
"""
from queue import PriorityQueue

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
            if not intervals:
                return 0
            
            pq = PriorityQueue()
            
            intervals.sort()
            pq.put(intervals[0][1])
            
            for record in intervals[1:]:
                if record[0] >= pq.queue[0]:
                    pq.get()
                pq.put(record[1])
                
            return len(pq.queue)