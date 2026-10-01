class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=prices[0]
        proft=0
        for i in range(0,len(prices)):
            if prices[i]<min:
                min=prices[i]
    
            if prices[i]-min>proft:
                proft=prices[i]-min
        return proft