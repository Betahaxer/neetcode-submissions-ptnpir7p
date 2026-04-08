class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestPrice = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i] - lowestPrice)
            lowestPrice = min(prices[i], lowestPrice)
        return maxProfit