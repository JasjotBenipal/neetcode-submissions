class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        drec_stack = [] #two values: temp, index

        for index, temp in enumerate(temperatures):
            while drec_stack and drec_stack[-1][0] < temp:
                res_temp, res_index = drec_stack.pop()
                result[res_index] = index - res_index
            drec_stack.append([temp, index])
        return result