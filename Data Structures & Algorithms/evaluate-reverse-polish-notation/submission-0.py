class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        def popstack(stack: List[str]) -> (str, str):
            x = stack.pop()
            y = stack.pop()
            return x, y
        
        def evaluate(x: str, y: str, op: str) -> str:
            a = int(x)
            b = int(y)

            if op == "+":
                res = a + b
                return str(res)
            elif op == "-":
                res = a - b
                return str(res)
            elif op == "*":
                res = a * b
                return str(res)
            elif op == "/":
                res = a / b
                return str(int(res))

        stack = []

        for tok in tokens:

            if tok not in ["+", "-", "*", "/"]:
                stack.append(tok)
            else:
                y, x = popstack(stack)
                temp = evaluate(x, y, tok)
                stack.append(temp)

        return int(stack[-1])