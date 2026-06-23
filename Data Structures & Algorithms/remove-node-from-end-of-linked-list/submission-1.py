# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        prev = head

        left, right = head, head
        i = 0
        while i != n and right:
            right = right.next
            i += 1

        while right != None:
            prev = left
            left = left.next
            right = right.next

        if i == n and prev == left:
            head = head.next
        elif i == n and prev:
            prev.next = left.next
        else:
            return None
        
        return head