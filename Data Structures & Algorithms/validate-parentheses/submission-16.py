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
                    False
            else:
                stack.append(char)
        print(stack)
        return True if not stack else False
         

        