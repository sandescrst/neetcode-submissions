class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest= prices[0]
        max_profit = 0

        for i in range(1,len(prices)):
            if prices[i] < cheapest:
                cheapest = prices[i]
            else:
                max_profit = max(max_profit, prices[i]-cheapest)
        
        return max_profit
