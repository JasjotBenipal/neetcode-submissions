# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.match = True

        def dfs(curr, comp):
            if not curr and not comp: return None
            
            if curr or comp:
                left = dfs(curr.left if curr else None, comp.left if comp else None)
                right = dfs(curr.right if curr else None, comp.right if comp else None)
                lval = curr.val if curr else None
                rval = comp.val if comp else None
                match = lval == rval
                if not match:
                    self.match = False
            return None
        dfs(p, q)
        return self.match