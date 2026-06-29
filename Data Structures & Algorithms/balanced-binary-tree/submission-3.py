# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.bal = True
        def dfs(curr):
            if not curr: return 0

            left = dfs(curr.left)
            right = dfs(curr.right)
            cur_bal = left == right or left == right + 1 or left + 1 == right
            if cur_bal == False: 
                self.bal = False
            return 1 + max(left, right)
        dfs(root)
        return self.bal