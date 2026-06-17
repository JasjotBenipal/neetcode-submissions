class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        leftout = 0
        rightout = len(matrix) - 1 

        while leftout <= rightout:
            midout = (leftout + rightout) // 2
            if matrix[midout][-1] < target:
                leftout = midout + 1
            elif matrix[midout][0] > target:
                rightout = midout - 1
            else:
                left = 0
                right = len(matrix[midout]) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if matrix[midout][mid] < target:
                        left = mid + 1
                    elif matrix[midout][mid] > target:
                        right = mid - 1
                    else:
                        return True
                return False
        return False
