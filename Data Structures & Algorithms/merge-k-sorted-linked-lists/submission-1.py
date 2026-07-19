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
    def merge(self, l1, l2):
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # return self.divide(0, len(lists) - 1, lists)

        if lists is None or len(lists) == 0:
            return None
        
        mergedList = lists
        while len(mergedList) > 1:
            temp = []
            for i in range(0, len(mergedList), 2):
                if i == len(mergedList) - 1:
                    temp.append(mergedList[i])
                else:
                    temp.append(self.merge(mergedList[i], mergedList[i + 1]))
            mergedList = temp
        return mergedList[0]
            