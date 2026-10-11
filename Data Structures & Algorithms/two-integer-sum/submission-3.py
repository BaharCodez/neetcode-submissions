class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        book = {}
        for i, num in enumerate(nums):
            if num in book:
                return [book[num], i]
            book[target - num] = i
            
            
        