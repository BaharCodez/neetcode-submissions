class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        trip = []
        for idx, num in enumerate(nums):
            i = idx + 1
            j = len(nums)-1
            print(i, j)
            while j > i:
                if num + nums[i] + nums[j] > 0:
                    j -=1

                elif num + nums[i] + nums[j] < 0:
                    i +=1
                
                else: 
                    print('yaya')
                    if [num, nums[i], nums[j]] not in trip:
                        trip.append([num, nums[i], nums[j]])
                    i+=1
                    


            
            #idx += 1
            
        return trip



        