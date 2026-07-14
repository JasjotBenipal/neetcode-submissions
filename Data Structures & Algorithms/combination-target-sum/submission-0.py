class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i, subset, total):
            if total == target:
                res.append(subset.copy())
            
            if total >= target or i >= len(nums):
                return
            
            # case 1: include nums[i] and repeat it
            subset.append(nums[i])
            dfs(i, subset, total + nums[i])

            #case 2: not nums[i] and never include it
            subset.pop()
            dfs(i + 1, subset, total)
        dfs(0, subset, 0)

        return res