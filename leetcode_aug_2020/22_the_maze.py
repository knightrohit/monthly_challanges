"""
Time/Space Complexity = O(m*n)
"""
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
       
        row, col = len(maze), len(maze[0])
        visited = set()
        
        def dfs(r, c):
            
            if (r, c) in visited:
                return False
            
            visited.add((r, c))
     
            if [r,c] == destination:
                return True
            
            for r1, c1 in (1,0), (-1,0), (0,1), (0,-1):
                nr, nc = r , c
                while 0 <= nr + r1 < row and 0 <= nc + c1 < col and maze[nr + r1][nc + c1] == 0:
                    nr += r1
                    nc += c1
                if dfs(nr, nc):
                    return True

            return False
        
        return dfs(*start)