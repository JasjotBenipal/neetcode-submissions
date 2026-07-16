class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        subset = []
        res.add(tuple([]))
        nums.sort()

        for num in range(len(nums)):
            resi = res.copy()
            for result in resi:
                copy = list(result)
                copy.append(nums[num])
                res.add(tuple(copy))
        resu = []
        for thing in res:
            resu.append(list(thing))
        return resu

