class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # pair: (index, height)
        maxarea = 0

        for index, height in enumerate(heights):
            left = index
            while stack and stack[-1][1] > height:
                maxarea = max(maxarea, stack[-1][1] * (index - stack[-1][0]))
                left = stack[-1][0]
                stack.pop()
            stack.append([left, height])

        for i, h in stack:
            maxarea = max(maxarea, (len(heights) - i) * h)

        return maxarea