class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        num_length = len(nums) -1

        for index, number in enumerate(nums):
            if index > 0 and number == nums[index - 1]:
                continue
            left, right = index + 1, num_length
            while left < right:
                sum = number + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    result.append([number, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
        return result