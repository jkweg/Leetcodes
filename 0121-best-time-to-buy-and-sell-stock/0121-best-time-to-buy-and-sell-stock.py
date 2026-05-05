class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l , r = 0 , 1

        maxi = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                maxi = max(prices[r] - prices[l] , maxi)
            else:
                l = r
            
            r += 1
        
        return maxi 