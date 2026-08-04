class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        minPrice = prices[0]
        maxPrice = 0
        for p in prices:
            if p < minPrice:
                minPrice = p
            else:
                temp = p - minPrice
            
            if temp > maxPrice:
                maxPrice = temp
        return maxPrice