"""
Time Complexity = O(N)
Space Complexity = O(D), D is the diameter of the tree
"""

from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        out = []
        queue = deque()
        queue.append((root, 0))
        prev_indx = 0
        prev_val = root.val
        node = None
        while queue:
            node, indx = queue.popleft()
            if indx == prev_indx:
                prev_val = node.val
            else:
                prev_indx = indx
                out.append(prev_val)
                prev_val = node.val
                
            if node.left:
                queue.append((node.left, indx + 1))
            if node.right:
                queue.append((node.right, indx + 1))
                
        out.append(node.val)
        return out