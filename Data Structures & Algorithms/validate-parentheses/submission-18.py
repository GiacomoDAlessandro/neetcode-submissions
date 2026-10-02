class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False
        l,r = 0, len(s) - 1

        open = ["[", "(", "{"]
        closed = ["]", ")", "}"]
        d = {")" : "(", "]" :"[", "}" : "{" }
        stack = []
        for i in s:
            if i in open:
                stack.append(i)
            else:
                if not stack:
                    return False
                t = stack.pop()
                if d[i] != t:
                    return False

            
        return not stack
            
