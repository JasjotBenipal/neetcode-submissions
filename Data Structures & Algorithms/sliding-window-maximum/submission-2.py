class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        que = deque()
        left = right = 0

        while right < len(nums):
            while que and nums[que[-1]] < nums[right]:
                que.pop()
            que.append(right)
            
            if left > que[0]:
                que.popleft()
            
            if right - left + 1 == k:
                result.append(nums[que[0]])
                left += 1
            
            right += 1
        return result

"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0 
        result = []

        for right in range(len(nums)):
            if right - left + 1 == k:
                result.append(max(nums[left : right + 1]))
                left += 1
        return result

Time: O(k * (n - k))
"""