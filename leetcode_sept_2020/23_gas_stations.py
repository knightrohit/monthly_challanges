"""
Time Complexity = O(N^2)
Space Complexity = O(1)
"""
# TLE error

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if not gas or not cost:
            return 0

        def travel(indx, tcost = 0, start = 0):

            if indx == len(gas) + start:
                return start
            
            tcost += gas[indx%len(gas)] - cost[indx%len(gas)]
            print(tcost)
            if tcost < 0:
                return -1
            else:
                return travel(indx+1, tcost, start)
        
        for indx in range(len(gas)):
            x = travel(indx, 0, indx)
            if x >= 0:
                return x


"""
Time Compleixty = O(N)
Space Complexity = O(1)
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if not gas or not cost:
            return 0
        
        total_cost = 0
        curr_cost = 0
        indx = 0

        for i in range(len(gas)):
            
            total_cost += gas[i] - cost[i]
            curr_cost += gas[i] - cost[i]
            if curr_cost < 0:
                curr_cost = 0
                indx = i + 1
        
        return indx if total_cost >= 0 else -1