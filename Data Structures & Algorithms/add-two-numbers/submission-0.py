# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        final = ListNode()
        summ = final
        while l1 or l2 or carry:
            s1, s2, s3 = 0, 0, 0
            if l1:
                s1 = l1.val
                l1 = l1.next
            if l2:
                s2 = l2.val
                l2 = l2.next
            
            if s1 + s2 + carry < 10:
                s3 = s1 + s2 + carry
                carry = 0
            else:
                s3 = s1 + s2 + carry - 10
                carry = 1
            
            n3 = s3
            summ.next = ListNode(n3)
            summ = summ.next
        
        return final.next
            
