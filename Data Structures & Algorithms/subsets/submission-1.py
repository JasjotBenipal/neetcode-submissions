class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Backtracking
        res = []

        subset = []

        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            # case 1: include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # case 2: don't include nums[i], rather [] instead
            subset.remove(nums[i])
            dfs(i + 1)
        dfs(0)
        return res

"""
Iterative solution
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        res.append([])
        
        for num in nums:
            for uniq in range(len(res)):
                copy = res[uniq].copy()
                copy.append(num)
                res.append(copy)
        return res

"""