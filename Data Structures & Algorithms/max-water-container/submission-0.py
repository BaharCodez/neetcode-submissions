class Solution:
    def maxArea(self, heights: List[int]) -> int:

        largest = 0

        i = 0
        j = len(heights) -1

        while j> i:
            if heights[i] < heights[j]:
                temp = heights[i] * ( j - i)
                if temp > largest:
                    largest = temp
                i +=1
            else:
                temp = heights[j] * ( j - i)
                if temp > largest:
                    largest = temp
                j -=1
        return largest