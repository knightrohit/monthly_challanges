"""
Time/Space Complexity = O(N)
"""
#DP: Top down
from functools import lru_cache

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        if 2*k >= len(prices):
            profit = 0
            for i in range(1, len(prices)):
                profit += max(prices[i] - prices[i-1], 0)                
            return profit
        
        
        @lru_cache(None)
        def buy_sell(indx, buy, k):

            if indx >= len(prices) or k <= 0:
                return 0
            
            # Buy or skip
            if buy:
                return max(-prices[indx] + buy_sell(indx+1, 0, k), buy_sell(indx+1, 1, k))
            
            # sell or skip
            else:
                return max(prices[indx] + buy_sell(indx+1, 1, k-1), buy_sell(indx+1, buy, k))
            
        return buy_sell(0,1,k)