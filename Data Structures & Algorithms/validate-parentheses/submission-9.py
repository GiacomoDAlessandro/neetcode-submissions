class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")": "(", "}": "{", "]": "["}


        for i in s:
            if i in brackets:
                if not stack or stack[-1] != brackets[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
                    

        return not stack
