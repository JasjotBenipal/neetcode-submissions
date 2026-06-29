# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.bal = True
        self.fin = True
        def dfs(curr):
            if not curr: return 0

            left = dfs(curr.left)
            right = dfs(curr.right)
            self.bal = left == right or left == right + 1 or left + 1 == right
            if self.bal == False: 
                self.fin = False
            return 1 + max(left, right)
        dfs(root)
        return self.fin