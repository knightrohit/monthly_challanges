"""
Time Complexity = O(N)
Space Complexity = O(1)
"""

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        
        start, end = 0, len(people) - 1
        boat = 0
        people_left = len(people)
        
        while people_left and start <= end:
            boat += 1
            if people[end] + people[start] <= limit:
                people_left -= 2
                start += 1
                end -= 1
            else:
                end -= 1
                people_left -= 1
            
        return boat