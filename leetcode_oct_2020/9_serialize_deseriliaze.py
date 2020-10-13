"""
Time/Space Complexity = O(N)
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        po = []
        def preorder(node):
            if not node:
                return
            po.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return ','.join(po)
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        po = list(map(int, data.split(',')))[::-1]
        
        def make(min_val = float('-inf'), max_val = float('inf')):

            if  po and min_val < po[-1] < max_val:
                val = po.pop()
                node = TreeNode(val)
                node.left = make(min_val, val)
                node.right = make(val, max_val)
                return node
            
        return make()