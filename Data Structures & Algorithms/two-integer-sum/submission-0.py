class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) -1
        while i < len(nums) -1:
            while i < j:
                if nums[i] + nums[j] == target:
                    return [i, j]
                j -=1
            i +=1


            
        