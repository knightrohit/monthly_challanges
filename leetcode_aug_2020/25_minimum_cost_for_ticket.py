"""
Time/Space Complexity = O(last day)
"""
from functools import lru_cache

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        last_date = days[-1]
        dayset = set(days)
        
        @lru_cache(None)
        def min_cost(days = 1):
            
            if days > last_date:
                return 0
            
            elif days in dayset:
                return min(min_cost(days + day) + cost for cost, day in zip(costs, [1,7,30]))            
            else:
                return min_cost(days + 1)            
        
        return min_cost()