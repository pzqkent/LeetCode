class Solution(object):
    def maxProfit(self, prices):
        return sum([max(prices[i+1] - prices[i], 0) for i in range(len(prices) - 1)])
        
#         profit  = 0
#         for i in range(len(prices)):
            

#             if cache 
        """
        :type prices: List[int]
        :rtype: int
        """