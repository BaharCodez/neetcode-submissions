class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset = set(nums)
        longest = 0
        
        for num in numset:
            length = 0
            if num -1 not in numset:
                length = 1

                while length + num in numset:
                    length +=1

            if length > longest:
                longest = length    

            
            
        return longest