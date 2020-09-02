"""
Time/Space complexity = O(1)
"""
# Approach using variables
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        time = ''

        for i, a in enumerate(A):
            for j, b in enumerate(A):
                for k, c in enumerate(A):
                    if i == j or j == k or k == i: continue
                    
                    d = A[6 - i - j - k]
                    hour = f'{a}{b}'
                    minute = f'{c}{d}'
                    if hour < '24' and minute < '60':
                        time = max(time, f'{hour}:{minute}')
                        
        return time


# Using permutations
from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        time = ''
        for a,b,c,d in permutations(A):
            hour, minute = f'{a}{b}', f'{c}{d}'
            
            if hour < '24' and minute < '60':
                time = max(time, f'{hour}:{minute}')
                
        return time