class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values = set()
        for number in nums:
            if number in values:
                return True
            else:
                values.add(number)
        return False