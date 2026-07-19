# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def divide(self, l, r, lists):
        if l > r:
            return None
        if l == r:
            return lists[l]
        
        mid = (l + r) // 2
        l = self.divide(l, mid, lists)
        r = self.divide(mid + 1, r, lists)

        return self.conquer(l, r)

    def conquer(self, l, r):
        if r is None:
            return l
        if l is None:
            return r
        
        dummy = ListNode()
        cur = dummy
        while l and r:
            if l.val < r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next

        if l:
            cur.next = l
        if r: 
            cur.next = r
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.divide(0, len(lists) - 1, lists)