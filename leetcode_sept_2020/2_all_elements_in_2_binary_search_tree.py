"""
Time/Space Complexity = O(N)
"""

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        out = []
        # Inorder traversal
        def dfs(node):
            return dfs(node.left) + [node.val] + dfs(node.right) if node else []
        
        list1 = dfs(root1)
        list2 = dfs(root2)
        
        i, j = 0, 0
        
        while i < len(list1) and j < len(list2):
            if list1[i] > list2[j]:
                out.append(list2[j])
                j += 1
                
            elif list2[j] > list1[i]:
                out.append(list1[i])
                i += 1
                
            else:
                out.extend([list1[i], list2[j]])
                i += 1
                j += 1
                
                
        if i < len(list1):
            out.extend(list1[i:])
        if j < len(list2):
            out.extend(list2[j:])            
                
        return out