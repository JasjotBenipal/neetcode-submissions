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