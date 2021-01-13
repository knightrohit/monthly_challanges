"""
Time/Space Complexity = O(N)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1 or not l2:
            return l1 or l2
        
        sum_node = ListNode()
        node = sum_node
        carry = 0
        
        while l1 or l2 or carry:
            add_val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            val = add_val % 10
            node.next = ListNode(val)
            carry = add_val // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            node = node.next
            
        return sum_node.next 