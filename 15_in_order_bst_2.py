"""
Time/Space Complexity = O(N)
"""
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        cnode = node
        if not cnode:
            return cnode
        
        # Find root node
        while cnode.parent:
            cnode = cnode.parent
            
        out = []
        def dfs(node):
            if not node:
                return node
            
            dfs(node.left)
            out.append(node)
            dfs(node.right)

        dfs(cnode)
        indx = out.index(node)
        return out[indx + 1] if indx + 1 <= len(out) - 1 else None
            
            

# Second Approach
"""
Time Complexity = O(log N)
Space Complexity = O(1)
"""
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        
        if not node:
            return node
        
        # node has right child
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        
        # node has no right child
        while node.parent and node.parent.right == node:
            node = node.parent
            
        return node.parent
        
    
    
        