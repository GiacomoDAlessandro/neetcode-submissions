class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                profit += prices[r] - prices[l]
                l += 1
                r = l + 1
            else:
                r += 1
                l += 1
        return profit