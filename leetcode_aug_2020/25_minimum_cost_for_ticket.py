"""
Time/Space Complexity = O(last day)
"""
# Top down DP
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


# Bottom Up DP
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        # dp[i] minimum cost till ith date
        dp = [0]*(days[-1] + 1)
        setdays = set(days)
        
        for i in range(1, days[-1]+1):
            if i not in setdays:
                dp[i] = dp[max(0,i-1)]
            else:
                #dp[i] = min(dp[max(0,i-1)]+costs[0], dp[max(0,i-7)]+costs[1], dp[max(0,i-30)]+costs[2])
                dp[i] = min(dp[(max(0, i-d))] + c for d, c in zip((1,7,30), costs))
            
        return dp[-1]