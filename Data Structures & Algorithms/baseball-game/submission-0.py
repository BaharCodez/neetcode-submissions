class Solution:
    def calPoints(self, operations: List[str]) -> int:
        '''
        use a stack. we add 1 and 2 to a stack. if we reach an operation then we pop apply operation to them. then move on with list. this should be O(n) speed becuase we iterate once through list. Then O(1) sapce as the stack stays small
        '''
        operands = []
        for char in operations:
            print(operands)
            if char == '+':
                a = operands[-1]
                b = operands[-2]
                operands.append(int(a) +int(b))
            elif char == 'D':
                operands.append(operands[-1]*2)
                
            elif char == 'C':  
                operands.pop()
            else:
                operands.append(int(char))  

        return sum((operands))