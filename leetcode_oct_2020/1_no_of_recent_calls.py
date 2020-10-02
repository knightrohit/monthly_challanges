"""
Time/Space Complexity = O(N)
"""

class RecentCounter:

    def __init__(self):
        self.requests = []        

    def ping(self, t: int) -> int:
        
        self.requests.append(t)
        
        if len(self.requests) == 1:
            return 1
        else:
            for indx, val in enumerate(self.requests):
                if val >= t - 3000:
                    self.requests = self.requests[indx:]
                    return len(self.requests)