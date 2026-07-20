# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = groupPrev = ListNode(0, head)
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            prev, cur = kth.next, groupPrev.next
            while cur != groupNext:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        return dummy.next

    def getKth(self, cur, k):
        count = 0
        while cur and count < k:
            cur = cur.next
            count += 1
        return cur

            