# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def insert(head,tail,val):
            if not head:
                head = ListNode(val)
                tail = head
            else:
                tail.next = ListNode(val)
                tail = tail.next
            return head,tail
        carry = 0
        head = None
        tail = None
        while l1 and l2:
            val = l1.val + l2.val + carry
            head,tail = insert(head,tail,val%10)
            carry = val//10
            l1 =l1.next
            l2 = l2.next
        while l1:
            val = l1.val + carry
            head,tail = insert(head,tail,val%10)
            carry = val//10
            l1 = l1.next
        while l2:
            val = l2.val + carry
            head,tail = insert(head,tail,val%10)
            carry = val//10
            l2 = l2.next
        if carry != 0:
            head,tail = insert(head,tail,carry)
        return head