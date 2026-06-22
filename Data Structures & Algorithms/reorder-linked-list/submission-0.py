# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get halfway
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse 2nd half
        rev = slow.next
        slow.next = None
        prev = None
        while rev:
            temp = rev.next
            rev.next = prev
            prev = rev
            rev = temp

        swi = prev

        #Join together
        
        curr = head
        while curr and prev:
            temp = curr.next
            temprev = prev.next
            curr.next = prev
            curr.next.next = temp
            curr = temp
            prev = temprev