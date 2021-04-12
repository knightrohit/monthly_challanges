"""
Time Complexity : O(N) worst, O(logN)
Space Complexity: O(1)
"""
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        if not root or not root.val:
            return None
            
        if root == p:
            return root.right
            
        successor = None
        node = root
        
        while node:
            if p.val >= node.val:
                node = node.right
                
            else:
                successor = node
                node = node.left
                
        return successor