"""
Time/Space Complexity = O(N)
"""

from collections import deque

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if not head:
            return head
        
        if k == 0:
            return head
        
        dq = deque()
        node = head
        
        while node:
            dq.append(node.val)
            node = node.next
       
        k %= len(dq)
        
        while k > 0:
            val = dq.pop()
            dq.appendleft(val)
            k -= 1
        
        head = node = ListNode()
        for i in dq:
            node.next = ListNode(i)
            node = node.next
            
        return head.next