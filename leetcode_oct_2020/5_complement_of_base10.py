"""
Time/Space Complexity = O(1)
"""
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0: return 1
        size = N.bit_length()
        mask = (1 << (size)) - 1
        return N ^ mask