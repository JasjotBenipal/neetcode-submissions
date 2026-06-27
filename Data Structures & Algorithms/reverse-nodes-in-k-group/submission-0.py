# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseNtimes(self, head, k) -> Optional[ListNode]:
        while head and k - 1 > 0:
            k -= 1
            head = head.next
        return head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        result = head
        curr = result
        prev_tail = None

        while True:
            cur_head = self.reverseNtimes(curr, k)

            if not cur_head:
                break

            next_head = cur_head.next
            prev = next_head
            tail = curr
            while curr and curr != next_head:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            if prev_tail == None:
                result = cur_head
            else:
                prev_tail.next = cur_head
            prev_tail = tail
        return result