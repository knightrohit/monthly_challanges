"""
Time Complexity < O(NlogN)
Space Complexity = O(N)
"""
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        
        nodes  = defaultdict(list)
        
        def dfs(node, x = 0, y = 0):

            if not node:
                return

            nodes[x].append((node.val, y))

            dfs(node.left, x - 1, y - 1)
            dfs(node.right, x + 1, y - 1)
            
        dfs(root)
        out = [sorted(nodes[key], key = lambda x: (x[1], -x[0]), reverse = True) for key in sorted(nodes)]
        final = []
        for rec in out:
            temp = []
            for item in rec:
                temp.append(item[0])                
            final.append(temp)
        return final