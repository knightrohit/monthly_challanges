"""
Time/Space Complexity = O(n1 + n2)
"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1 or not l2:
            return l1 or l2
        
        node = l1
        list1, list2 = [], []
        
        while node:
            list1.append(str(node.val))
            node = node.next
            
        node = l2
        while node:
            list2.append(str(node.val))
            node = node.next
            
        n1 = ''.join(list1)
        n2 = ''.join(list2)
        s = str(int(n1) + int(n2))
        
        root = ListNode(int(s[0]))
        node = root
        for i in s[1:]:
            node.next = ListNode(int(i))
            node = node.next            
        return root