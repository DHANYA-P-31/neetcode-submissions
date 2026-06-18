# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        temp = slow.next
        slow.next = None
        prev = None
        while temp:
            t = temp.next
            temp.next = prev
            prev = temp
            temp = t
        temp = head
        while prev:
            t = temp.next
            temp.next = prev
            s = prev.next
            prev.next = t
            temp = t
            prev= s