"""
Time/space complexity = O(logN)
"""
class Solution:
    
    def successor(self, node):
        node = node.right
        while node.left:
            node = node.left
        return node.val
    
    def predeccessor(self, node):
        node = node.left
        while node.right:
            node = node.right
        return node.val            
            
        
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
            
        else:
            #if root is a leaf
            if not (root.left or root.right):
                root = None
                
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
                
            else:
                root.val = self.predeccessor(root)
                root.left = self.deleteNode(root.left, root.val)
                
        return root