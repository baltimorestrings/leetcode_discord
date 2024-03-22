class Solution2:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        buy_price = prices[0]
        for i in range(1, len(prices)):
            buy_price = min(buy_price, prices[i])
            max_profit = max(max_profit, prices[i] - buy_price)
        return max_profit


print(Solution2().maxProfit([7, 6, 4, 3, 1]))
