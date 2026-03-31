class Solution(object):
        def maxProfit(self, prices):
            totalProfit = 0
            for i in range(0, len(prices)-1):
                if prices[i]<prices[i+1]:
                    totalProfit += prices[i+1] - prices[i]
            return totalProfit