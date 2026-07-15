class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(subset, num):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            for n in range(len(nums)):
                if not num[n]:
                    subset.append(nums[n])
                    num[n] = True
                    dfs(subset, num)
                    subset.pop()
                    num[n] = False

        dfs(subset, [False] * len(nums))
        return res