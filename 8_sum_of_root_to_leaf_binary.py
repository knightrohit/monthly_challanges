"""
Time/space complexity = O(N)
"""
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        out = []

        def dfs(node, val=''):
            
            if not node:
                return 

            if not (node.left or node.right):
                return out.append(int(''.join(val)+ str(node.val), 2))
            
            val += str(node.val)
            dfs(node.left, val)
            dfs(node.right, val)
        
        dfs(root)
        return sum(out)