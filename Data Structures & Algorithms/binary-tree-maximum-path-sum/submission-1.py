# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = root.val
        def dfs(root):
            if not root: return 0
            suml = dfs(root.left)
            sumr = dfs(root.right)
            suml = suml if suml > 0 else 0
            sumr = sumr if sumr > 0 else 0
            sumtotal = suml + sumr + root.val
            self.max_sum = max(sumtotal, self.max_sum)
            return root.val + max(suml, sumr)
        dfs(root)
        return self.max_sum