# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        t1 = list1
        t2 = list2
        head, tail = None, None
        def insert(head,tail,value):
            node = ListNode(value)
            if not head:
                head = tail = node
            else:
                tail.next = node
                tail = tail.next
            return (head,tail)
        while t1 and t2:
            if t1.val < t2.val:
                (head,tail) = insert(head,tail,t1.val)
                t1 = t1.next
            else:
                (head,tail) = insert(head,tail,t2.val)
                t2 = t2.next
        while t1:
            (head,tail) = insert(head,tail,t1.val)
            t1 = t1.next
        while t2:
            (head,tail) = insert(head,tail,t2.val)
            t2 = t2.next
        return head