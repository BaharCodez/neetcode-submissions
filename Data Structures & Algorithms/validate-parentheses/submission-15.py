class Solution:
    def isValid(self, s: str) -> bool:
        # Edge case: starting with a close bracket, empty

        stack = []

        closeToOpen = {")": "(", "]": "[", "}": "{"}
        
        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
            else:
                stack.append(char)
        print(stack)
        if len(stack) ==0:
             return True
        else:
            return False

        