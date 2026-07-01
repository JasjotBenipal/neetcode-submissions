# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0

        def dfs(root, max_rn):
            if root == None:
                return None

            if root.val >= max_rn:
                self.good += 1
                max_rn = root.val
            
            dfs(root.left, max_rn)
            dfs(root.right, max_rn)

        dfs(root, float("-inf"))
        return self.good