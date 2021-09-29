"""
Time Complexity = O(n log n)
Space Complexity = O(n)
"""
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        if not arr:
            return arr
        
        return list(map({val: indx + 1 for indx, val in enumerate(sorted(set(arr)))}.get, arr))