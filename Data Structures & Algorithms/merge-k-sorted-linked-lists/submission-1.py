# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Node:
    def __init__(self, node):
        self.stored_ListNode = node

    def __lt__(self, compare_node):
        return self.stored_ListNode.val < compare_node.stored_ListNode.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        dummy = ListNode()
        result = dummy

        heap = []
        
        for k in lists:
            if k:
                heapq.heappush(heap, Node(k))

        while heap:
            result.next = heapq.heappop(heap).stored_ListNode
            result = result.next
            if result.next:
                heapq.heappush(heap, Node(result.next))
        
        return dummy.next