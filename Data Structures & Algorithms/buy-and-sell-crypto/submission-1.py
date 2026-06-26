class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        maxProfit = 0
        L = 0
        for R in range(len(prices)):
            profit = prices[R] - prices[L]
            maxProfit = max(maxProfit, profit)

            if prices[R] < prices[L]:
                L = R
        
        return maxProfit





            
            

        