
"""
Time Complexity = O(1) average, worst case - O(∞)
Space Compleixty = O(1)
"""
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        row, col, indx = 0, 0, 41
        
        while indx > 40:
            row, col = rand7(), rand7()
            indx = (row - 1)*7 + col
            
        return (indx - 1)%10 + 1