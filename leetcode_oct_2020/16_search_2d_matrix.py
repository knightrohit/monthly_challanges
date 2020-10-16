"""
Time Complexity = O(logN)
Space Compleixty = O(N)
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix:
            return False
        
        n_list = []
        for i in matrix:
            n_list.extend(i)
            
        start, end = 0, len(n_list) - 1
        while start <= end:
            mid = (start + end)//2
            if n_list[mid] == target:
                return True
            
            elif n_list[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
                
        return False