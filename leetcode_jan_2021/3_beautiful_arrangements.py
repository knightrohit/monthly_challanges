"""
Time/Space Complexity - O(N)
"""
class Solution:
    def countArrangement(self, n: int) -> int:

        self.visited = [False]*(n+1)
        self.count = 0
        
        def calculate(indx, n):
 
            if indx > n:
                self.count += 1
                return
            
            for i in range(1, n+1):
                if not self.visited[i] and (i%indx == 0 or indx%i == 0):
                    self.visited[i] = True
                    calculate(indx+1, n)
                    self.visited[i] = False
                    
        calculate(1, n)
        return self.count