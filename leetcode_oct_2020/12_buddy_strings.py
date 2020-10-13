"""
Time/Space Complexity = O(N)
"""

from collections import Counter

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        
        if not A or len(A) == 1 or len(A) != len(B):
            return False
        
        if A == B:
            for i in Counter(A).values():
                if i >= 2:
                    return True

            return False
        
        count = []

        for i, j in zip(A, B):
            if i != j:
                count.append((i,j))
                
            if len(count) >= 3:
                return False
                
        return len(count) == 2 and count[0][0] == count[1][1] and count[0][1] == count[1][0]