"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = {}
        temp = head
        while temp:
            node = Node(temp.val)
            copy[temp] = node
            temp = temp.next
        new_head = copy[head] if head else None
        temp = head
        while temp:
            copy[temp].next = copy[temp.next] if temp.next else None
            copy[temp].random = copy[temp.random] if temp.random else None
            temp = temp.next
        return new_head
