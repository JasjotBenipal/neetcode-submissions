# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.smal = 0
        def dfs(node, k):
            if not node: 
                return -1
            
            val = dfs(node.left, k)
            self.smal += 1
            if self.smal == k:
                return node.val
            val2 = dfs(node.right, k)
            
            return max(val, val2)
        return dfs(root, k)