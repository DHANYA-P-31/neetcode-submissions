# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy
        while True:
            kth = self.getk(prev,k)
            if not kth:
                break
            gnext = kth.next
            p,c = kth.next,prev.next
            while c!= gnext:
                tmp = c.next
                c.next = p
                p = c
                c = tmp
            tmp = prev.next
            prev.next = kth
            prev = tmp
        return dummy.next
    def getk(self,head, k):
        temp = head
        while temp and k>0:
            temp = temp.next
            k -= 1
        return temp