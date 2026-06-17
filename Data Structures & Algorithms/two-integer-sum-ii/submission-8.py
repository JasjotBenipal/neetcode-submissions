"""
target: 7
[-11, -3, 5, 6, 10, 11]
[1, 3, 4, 5, 7, 11]
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left + 1, right + 1]
           