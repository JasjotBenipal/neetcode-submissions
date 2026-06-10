class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        profit = 0
        for index in range(len(prices)):
            if prices[index] < mini:
                mini = prices[index]
            profit = max(profit, prices[index] - mini)
        return profit