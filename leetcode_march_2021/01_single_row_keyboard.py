"""
Time/Space Complexity = O(N)
"""

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        
        indx_dict = {}
        total_time = 0
        curr_indx = 0
        
        for indx, val in enumerate(keyboard):
            indx_dict[val] = indx
            
        
        for i in word:
            total_time += abs(curr_indx - indx_dict[i])
            curr_indx = indx_dict[i]
            
        return total_time