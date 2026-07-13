# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # carry = 0
        # prev = ListNode()
        # res = prev
        # while l1 and l2:
        #     cur = ListNode(0)
        #     cur_node_val = l1.val + l2.val + carry
        #     cur.val = cur_node_val % 10
        #     carry = cur_node_val // 10 
        #     prev.next = cur
        #     prev = cur
        #     l1 = l1.next
        #     l2 = l2.next
        
        # while l1 or l2 or carry:
        #     cur = ListNode(0)
        #     if l1:
        #         cur_node_val = l1.val + carry
        #         l1 = l1.next
        #     elif l2:
        #         cur_node_val = l2.val + carry
        #         l2 = l2.next
        #     else: 
        #         cur_node_val = carry
        #     cur.val = cur_node_val % 10
        #     carry = cur_node_val // 10
        #     prev.next = cur
        #     prev = cur

        # return res.next
        def add(l1, l2, carry):
            if not l1 and not l2 and carry == 0:
                return None
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sum = v1 + v2 + carry
            carry = sum // 10
            digit = sum % 10
            cur = ListNode(digit, add(l1.next if l1 else None, l2.next if l2 else None, carry)) 
            return cur
        return add(l1, l2, 0)
            
        