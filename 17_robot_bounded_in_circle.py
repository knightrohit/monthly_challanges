"""
Time Complexity = O(N)
Space Complexity = O(1)
"""
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        if not instructions:
            return False
        
        x, y = 0, 0
        dirc = 'N'
        d_dict = {'N':(0,1), 'W':(-1,0), 'S':(0,-1), 'E':(1,0)}
        dl = {'N':'W', 'W':'S', 'S':'E', 'E': 'N'}
        dr = {'N':'E', 'W':'N', 'S':'W', 'E':'S'}

        for indx, i in enumerate(instructions*4):
            if i == 'G':
                dx, dy = d_dict[dirc]
                x += dx
                y += dy
                    
            elif i == 'L':
                dirc = dl[dirc]
            else:
                dirc = dr[dirc]
            
            if (x, y) == (0,0) and (indx+1)%len(instructions) == 0:
                return True
            
        return False