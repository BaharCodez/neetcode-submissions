class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        minPrice = prices[0]
        maxPrice = 0
        for p in prices:
            minPrice = min(minPrice, p)
            profit = p - minPrice
            
            maxPrice = max(maxPrice, profit)

        return maxPrice