# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        temp = slow.next
        slow.next = None
        while temp:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        temp = head
        while prev:
            t = temp.next
            temp.next = prev
            p = prev.next
            prev.next = t
            prev = p
            temp = t