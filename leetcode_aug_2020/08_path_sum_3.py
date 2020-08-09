"""
Time/Space Complexity = O(N)
"""

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        def dfs_with_parent(node, sum):
            count = 0
            if not node:
                return 0
            
            if node.val == sum:
                count += 1
            
            count += dfs_with_parent(node.left, sum - node.val) + dfs_with_parent(node.right, sum - node.val)
            return count
        
        if not root:
            return 0
        return self.pathSum(root.left, sum) + dfs_with_parent(root, sum) + self.pathSum(root.right, sum)