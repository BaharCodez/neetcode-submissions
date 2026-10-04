class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # brute force solution
    
        counter = 0
        for num in nums:
            counter +=1
            if num == target:
                return counter -1
        return -1
