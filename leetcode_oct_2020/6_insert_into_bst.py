"""
Time/Space complexity = O(log N)
"""
# Recursion
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if not root:
            return TreeNode(val)        
        
        def dfs(node):
            
            if not node:
                return node
      
            if val < node.val:
                if not dfs(node.left):
                    node.left = TreeNode(val)
            else:
                if not dfs(node.right):
                    node.right = TreeNode(val)
            
            return node
        
        return dfs(root)


# Second Approach (Recursion)
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:   
        
        def dfs(node):
            
            if not node:
                return TreeNode(val)
      
            if val < node.val:
                node.left = dfs(node.left)
            else:
                node.right = dfs(node.right)
            
            return node
        
        return dfs(root)


"""
Time Complexity = O(log N)
Space Complexity = O(1)
"""
#Iterative

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if not root:
            return TreeNode(val)
        
        node = root

        while node:
            prev = node
            if val < node.val:
                if not node.left:
                    node.left = TreeNode(val)
                    break
                node = node.left
                
            else:
                if not node.right:
                    node.right = TreeNode(val)
                    break
                node = node.right
            
        return root