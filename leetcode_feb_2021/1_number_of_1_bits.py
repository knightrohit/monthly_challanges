"""
Time Complexity = O(N), N = Number of bits
Space Complexity = O(1)
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


# Approach 2
"""
Time Compleixty = O(N), N = Number of 1 bits
Space Complexity = O(1)
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        no = 0
        
        while n != 0:
            n &= n - 1
            no += 1
            
        return no