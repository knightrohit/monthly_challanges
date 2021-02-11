"""
Time/Space Complexity = O(N)
"""
class Solution:
    def __init__(self):
            self.total = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        if root:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)            
        return root