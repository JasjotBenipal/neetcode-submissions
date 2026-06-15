class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        prefix = 1
        for index in range(len(nums)):
            answer[index] = prefix
            prefix *= nums[index]
        postfix = 1
        for jedex in range(len(nums) - 1, -1 , -1):
            answer[jedex] *= postfix
            postfix *= nums[jedex]
        return answer