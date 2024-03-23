def maxProfit(prices: list[int]) -> int:
    """
    We will track two things, lowest price seen (A), and max profit (B) we can make on the current one.

    We just keep retesting B on each one, and grabbing each new lowest stock point, and we're guaranteed to capture
    the longest line.
    """
    max_profit = 0
    buy_price = float('inf')
    for i in range(0, len(prices)):
        buy_price = min(buy_price, prices[i]) # A
        max_profit = max(max_profit, prices[i] - buy_price) # B
    return max_profit

def maxProfit2(prices: list[int]) -> int:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solutions/4868897/most-optimized-kadane-s-algorithm-java-c-python-rust-javascript/

    This is also O(N), O(1). Included it for completionism, but the first way is fine. Kadane's will come up in the
    largest subarray problem, so I figured might want it later.
    """
    n = len(prices)
    maxProfit = 0
    currMax_Profit = 0

    for i in range(1, n):
        currMax_Profit += prices[i] - prices[i - 1]

        if currMax_Profit > 0:
            pass

        else:
            currMax_Profit = 0

        maxProfit = max(maxProfit, currMax_Profit)

    return maxProfit
