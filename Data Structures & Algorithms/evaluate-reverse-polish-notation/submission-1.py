class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        token = tokens.pop()
        
        if token not in "+*-/":
            return int(token)
        
        right = self.evalRPN(tokens)
        left = self.evalRPN(tokens)

        if token == "+":
            return right + left
        elif token == "*":
            return right * left
        elif token == "-":
            return left - right
        elif token == "/":
            return int(left / right)