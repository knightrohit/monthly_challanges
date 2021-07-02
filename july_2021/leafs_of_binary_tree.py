"""
Time/Space Complexity = O(N)
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        out = []
        def po(node):
            if not node:
                return -1
            
            left_height = po(node.left)
            right_height = po(node.right)
            curr_height = 1 + max(left_height, right_height)
            out.append((node.val, curr_height))
            return curr_height
            
        height = po(root)
        
        leaves = []
        print(out)
        for val, indx in out:
            if len(leaves) > indx:
                leaves[indx].append(val)
            else:
                leaves.insert(indx, [val])
        return leaves