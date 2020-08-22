"""
Time Complexity = O(N)
Space Complexity = O(1)
"""

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if not A:
            return A
        
        p1, p2 = 0, len(A) - 1
        
        while p1 < p2:
            
            if A[p1] % 2 and A[p2] % 2 == 0:
                A[p1], A[p2] = A[p2], A[p1]
                
            if A[p1] % 2 == 0: p1 += 1
            if A[p2] % 2: p2 -= 1
                
        return A