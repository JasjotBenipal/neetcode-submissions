class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0 
        result = []

        for right in range(len(nums)):
            if right - left + 1 == k:
                result.append(max(nums[left : right + 1]))
                left += 1
        return result