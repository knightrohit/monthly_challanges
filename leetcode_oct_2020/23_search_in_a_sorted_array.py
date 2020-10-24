"""
Time Complexity = O(log T)
Space Complexity = O(1)
"""
class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """        
        prev, curr = 0, 1
        
        if reader.get(prev) == target:
            return prev
        
        while reader.get(curr) != 2147483647:
            if reader.get(curr) == target:
                return curr
            
            elif reader.get(curr) < target:
                prev = curr
                curr *= 2
            else:
                break

        # Binary Search
        while prev <= curr:
            mid = (prev + curr) // 2

            if reader.get(mid) == target:
                return mid

            elif reader.get(mid) > target:
                curr = mid - 1
            else:
                prev = mid + 1

        return -1