class Solution:
    def isValid(self, s: str) -> bool:
        # Edge case: starting with a close bracket, empty

        stack = []

        for char in s:
            if char == '(':
                stack.append(')')
            if char == '{':
                stack.append('}')
            if char == '[':
                stack.append(']')
            elif len(stack) > 0 and char == stack[-1]:
                #print(stack)
                stack.pop()
            else:
                return False

        if len(stack) ==0:
             return True
        else:
            return False

        