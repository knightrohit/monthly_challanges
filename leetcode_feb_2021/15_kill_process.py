"""
Time/Space complexity = O(N)
"""
from collections import defaultdict

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        
        adj_dict = defaultdict(list)
        out = [kill]

        for ind, val in enumerate(ppid):
            adj_dict[val].append(pid[ind])
            
        def killp(kill):
            for child in adj_dict.get(kill, []):
                out.append(child)
                killp(child)
                
        killp(kill)
        return out