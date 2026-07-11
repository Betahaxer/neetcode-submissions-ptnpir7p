# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        prev = ListNode()
        res = prev
        while l1 and l2:
            cur = ListNode(0)
            cur_node_val = l1.val + l2.val + carry
            cur.val = cur_node_val % 10
            carry = cur_node_val // 10 
            prev.next = cur
            prev = cur
            l1 = l1.next
            l2 = l2.next
        
        while l1 or l2:
            cur = ListNode(0)
            if l1:
                cur_node_val = l1.val + carry
                l1 = l1.next
            else:
                cur_node_val = l2.val + carry
                l2 = l2.next
            cur.val = cur_node_val % 10
            carry = cur_node_val // 10
            prev.next = cur
            prev = cur
            
        if carry != 0: 
            prev.next = ListNode(carry, None)
        return res.next
            
        