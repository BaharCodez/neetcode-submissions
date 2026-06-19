class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1]
        r = [1]
        j = len(nums)-1
        final_arr = []
        for i in range(len(nums)-1):
            l.append(l[i]*nums[i])
            i +=1

        while j > 0:
            r.insert(0 , r[0]*nums[j])
            j -=1
        
        k = 0

        while k < len(nums):
            final_arr.append(r[k]*l[k])
            k +=1
            

        return final_arr

        