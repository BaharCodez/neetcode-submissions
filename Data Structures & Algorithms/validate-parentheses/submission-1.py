class Solution:
    def isValid(self, s: str) -> bool:
        # Edge case: starting with a close bracket, empty

        stack = []

        for char in s:
            if char == '(' or '[' or '{':
                stack.append(char)
            elif char == stack.head():
                stack.pop()
            else: 
                return False
        return True

        