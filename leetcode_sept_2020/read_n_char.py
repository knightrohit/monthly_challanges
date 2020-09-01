"""
Time Complexity = O(N)
Space Complexity = O(1)
"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        buf4 = ['']*4
        copied = 0
        read = 4

        while copied < n and read == 4:
            read = read4(buf4)
            for i in range(read):
                buf[copied] = buf4[i]
                copied += 1
                if copied == n:
                    return copied
                
        return copied