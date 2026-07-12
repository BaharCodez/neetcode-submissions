class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        i = 0
        j = i + 1

        while i < len(temperatures) - 1:
            if temperatures[j] > temperatures[i]:
                stack.append(j - i)
                i += 1
                j = i + 1
            elif temperatures[j] <= temperatures[i] and j < len(temperatures) - 1: 
                j += 1
            else: 
                i += 1
                j = i + 1
                stack.append(0)
            
       
        stack.append(0)
        return stack

        


        
        