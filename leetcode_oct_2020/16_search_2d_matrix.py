"""
Time Complexity = O(RlogC)
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


"""
Time Complexity = O(RlogC)
Space Complexity = O(1)
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix:
            return False        
            
        for n_list in matrix:
            start, end = 0, len(n_list) - 1
            while start <= end:
                mid = (start + end)//2
                if n_list[mid] == target:
                    return True

                elif n_list[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1



"""
Time Complexity = log(row*col)
Space Complexity = O(1)
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix:
            return False        
            
        row, col = len(matrix), len(matrix[0])

        start, end = 0, row * col - 1

        while start <= end:
            mid = (start + end)//2

            if matrix[mid//col][mid%col] == target:
                return True

            elif matrix[mid//col][mid%col] > target:
                end = mid - 1
            else:
                start = mid + 1
                
        return False
        
                
        return False