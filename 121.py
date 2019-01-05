class Solution(object):
    def maxProfit(self, prices):
        if len(prices) == 0 or len(prices) == 1:
            return 0
        
        maxprofit = 0
        # print maxprofit
        current_buy = prices[0]
        for i in range(1,len(prices)):
            profit = prices[i] - current_buy
            # print profit
            
            if prices[i] < current_buy:
                current_buy = prices[i]
            maxprofit = max(maxprofit, profit)
            
            # for j in range(i + 1, len(prices)):
        # print maxprofit
        return maxprofit
                
            
        """
        :type prices: List[int]
        :rtype: int
        """
        