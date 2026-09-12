# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        t1 = list1
        t2 = list2
        head = node
        while t1 and t2:
            if t1.val < t2.val:
                node.next= ListNode(t1.val)
                t1 = t1.next
            else:
                node.next = ListNode(t2.val)
                t2 = t2.next
            node = node.next
        while t1:
            node.next= ListNode(t1.val)
            t1 = t1.next   
            node = node.next
        while t2:
            node.next= ListNode(t2.val)
            t2 = t2.next
            node = node.next

        return head.next   