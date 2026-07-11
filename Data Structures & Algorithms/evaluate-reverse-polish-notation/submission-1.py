class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }
        for token in tokens:
            if token not in operators:
                    stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(int(operators[token](a, b)))
        return stack.pop()
            
        