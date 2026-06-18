class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ind, res = -1, nums[0]

        left, right = 0, len(nums) - 1

        while left <= right:
            
            mid = (left + right) // 2
            if nums[mid] == target:
                ind = mid
                break
            if nums[left] <= nums[mid] and target < nums[mid] and target >= nums[left]:
                right = mid - 1
            elif nums[left] <= nums[mid] and (target > nums[mid] or target < nums[left]):
                left = mid + 1
                print(left)
            elif nums[left] > nums[mid] and (target < nums[mid] or target >= nums[left]):
                right = mid - 1
            elif nums[left] > nums[mid] and (target > nums[mid] and target < nums[left]):
                left = mid + 1
            

        return ind