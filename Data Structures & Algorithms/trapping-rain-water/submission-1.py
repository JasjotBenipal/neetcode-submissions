class Solution:
    
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        LMax = height[left]
        RMax = height[right]
        result = 0

        while left < right:
            minH = min(LMax, RMax)
            if LMax < RMax:
                left += 1
                LMax = max(height[left], LMax)
                result += LMax - height[left]
            else:
                right -= 1
                RMax = max(height[right], RMax)
                result += RMax - height[right]
        return result
    """
    this is wrong, finds local max area
    def trap(self, height: List[int]) -> int:
        
        total_area = 0
        
        
        for index in range(len(height)):
            left, right = index, len(height) - 1
            local_area = 0
            while left < right:
                area = self.calculate_area(left, right, height)
                local_area = max(local_area, area)
                if height[left] < height[right]:
                    left += 1
                else: 
                    right -= 1
            local_area = max(local_area, 0)
            total_area += local_area
            print(total_area)
        return total_area
        

    def calculate_area(self, left, right, height) -> int:
        result = 0
        for i in range(left + 1, right):
            minh = min(height[left], height[right])
            if height[i] < minh:
                result += minh - height[i]
            else: 
                return 0
        return result
        """