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
        store = {}

        first = head

        while first:
            store[first] = Node(0)
            first = first.next
        
        second = head
        
        dummy = store[head] if head else None
        final = dummy
        while second:
            final.val = second.val
            final.next = store[second.next] if second.next else None
            final.random = store[second.random] if second.random != None else None
            final = final.next
            second = second.next
        return dummy