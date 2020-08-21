"""
Time Complexity = O(N)
Space Complexity = O(1)
"""
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        # Find middle
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            
        # Reverse the second half
        curr, prev = slow, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
            
            
        # Merge two link list
        first, second = head, prev
        while second.next:           
            first.next, first = second, first.next
            second.next, second = first, second.next