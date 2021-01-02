"""
Time Complexity = O(N)
Space Coomplexity = O(W)
"""

from collections import deque

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        if not original or not cloned:
            return None
        
        queue = deque()
        queue.append(original)
        count = 0
        
        while queue:
            node = queue.popleft()
            count += 1
            if node == target:
                break
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        queue2 = deque()
        queue2.append(cloned)

        while queue2:
            node = queue2.popleft()
            count -= 1
            if node.val == target.val and count == 0:
                return node
            if node.left:
                queue2.append(node.left)
            if node.right:
                queue2.append(node.right)