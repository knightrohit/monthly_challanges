"""
Time/Space complexity = O(N)
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        out = []
        node = head

        while node:
            out.append(node.val)
            node = node.next
        
        nh = nnode = ListNode()

        for i in sorted(out):
            nnode.next = ListNode(i)
            nnode = nnode.next
        
        return nh.next
        