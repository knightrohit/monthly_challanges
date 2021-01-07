"""
Time Complexity = O(N)
Space Complexity = O(1)
"""

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        if not arr:
            return arr
        
        set_arr = set(arr)
        
        for i in range(1, arr[-1]+1):
            if i not in set_arr:
                k -= 1
                if k == 0:
                    return i
                
        if k:
            return arr[-1]+k