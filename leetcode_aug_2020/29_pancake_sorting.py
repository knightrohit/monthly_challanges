"""
Time Complexity = O(N^2)
Space Complexity = O(N)
"""

class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        
        out = []
        
        for i in range(len(A), 0, -1):
            
            ind = A.index(i)
            if ind == i - 1:continue
            elif ind != 0:
                out.append(ind+1)
                A[:ind+1] = A[ind::-1]
            
            out.append(i)
            A[:i] = A[i-1::-1]            
            
        return out