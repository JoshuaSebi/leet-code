class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP,curr=0,prices[0]
        for i in range(0,len(prices)):
            curr=min(curr,prices[i])
            maxP=max(maxP,prices[i]-curr)
        return maxP