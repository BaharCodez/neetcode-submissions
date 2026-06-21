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
            if char == '(':
                if char == stack[-1]:
                    stack.pop()
            if char == ']':
                if char == stack[-1]:
                    stack.pop()
            if char == '}':
                if char == stack[-1]:
                    stack.pop()


        if len(stack) ==0:
             return True
        else:
            return False

        