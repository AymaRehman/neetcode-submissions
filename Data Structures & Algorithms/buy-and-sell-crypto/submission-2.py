class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = [0]

        for b in range(len(prices)):
            for s in range(b + 1, len(prices)):
                p = prices[s] - prices[b]

                if p < 0:
                    p = 0

                profit.append(p)

        return max(profit)
