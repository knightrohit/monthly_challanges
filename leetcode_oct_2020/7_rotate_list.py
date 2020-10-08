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


"""
Time Complexit = O(N)
Space Complexity = O(1)
"""

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if not head:
            return head
        
        if k == 0:
            return head

        node = head
        size = 0
        while node.next:
            node = node.next
            size += 1
        node.next = head
        size += 1

        k %= size 
        
        node = head
        for _ in range(size - (k + 1)):
            node = node.next
        
        head = node.next
        node.next = None

        return head