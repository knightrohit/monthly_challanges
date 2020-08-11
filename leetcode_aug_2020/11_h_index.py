"""
Time Complexity = O(NlogN)
Space Complexity = O(1)
"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_indx = 0
        
        for indx, val in enumerate(sorted(citations, reverse = True)):
            
            if val >= indx + 1:
                h_indx += 1
            else:
                break
                
        return h_indx 