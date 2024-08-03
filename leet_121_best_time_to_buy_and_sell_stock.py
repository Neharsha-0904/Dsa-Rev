class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mp=float('inf')
        p=0
        for i in prices:
            if i<mp:
                mp=i
            elif i-mp>p:
                p=i-mp
        return p