"""
Time Complexity = O(n)
Space Complexity = O(1)
"""

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        if not head or not head.next:
            return False
        
        sp = head
        fp = head
        
        while fp:
            if sp.next:
                sp = sp.next                
            else:
                return False
            
            if fp.next and fp.next.next:
                fp = fp.next.next
            else:
                return False
            
            if sp == fp:
                return True