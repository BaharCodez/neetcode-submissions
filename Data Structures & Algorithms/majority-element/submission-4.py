class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # For if we want to scan it once we could add how many times a number comes in a scan and then pick the one with most using a hashmAP
        #we would weant the key to be the number the value to be the count
        count = {}
        majority = len(nums)//2
        for num in nums:

            if num in count:
                count[num] += 1
                if count[num] > majority:
                    return num
            else:
                count[num] = 1

        return nums[0]
        