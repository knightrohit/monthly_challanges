"""
Time/Space complexity = O(N)
"""
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        
        def trim(node):
            if not node:
                return node
            
            if node.val < low:
                return trim(node.right)
            
            elif node.val > high:
                return trim(node.left)
            
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node
            
        return trim(root)