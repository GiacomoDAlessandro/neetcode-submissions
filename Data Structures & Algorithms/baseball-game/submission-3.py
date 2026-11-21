class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = 0
        s = []
        for i in operations:
            if i == "+":
                res = s[len(s) - 1] + s[len(s) - 2]
                s.append(res)
            elif i == "C":
                s.pop()
            elif i == "D":
                res = s[len(s) - 1] * 2
                s.append(res)
            else:
                s.append(int(i))
        res = 0
        for i in s:
            res += i
        return res