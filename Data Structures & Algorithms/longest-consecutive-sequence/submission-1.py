class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        longest = 0

        for number in nums:
            if (number - 1) in store:
                continue
            temp = number
            streak = 0
            while temp in store:
                streak += 1
                temp += 1
            longest = max(streak, longest)
        return longest

"""
optimized/ diff is using store instead of nums during for loop for duplicate,
using streak instead of temp variable, 
starting streak at 1 instead of 0 to count current in while loop b/c in for loop store:
for number in store:
    if (number - 1) not in store:
        streak = 1
        while (number + streak) in store:
            streak += 1
        longest = max(streak, longest)
return longest
"""