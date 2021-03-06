"""
Time/Space Complexity = O(N)
"""

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        lkp = set()
        out = []
        for i in nums:
            if i not in lkp:
                lkp.add(i)
            else:
                out.append(i)

        val = list(set(range(1, len(nums)+1)) - lkp)[0]
        out.append(val)
        return out