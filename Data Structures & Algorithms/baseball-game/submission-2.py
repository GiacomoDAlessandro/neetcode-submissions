class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = 0
        s = []
        for i in operations:
            if i == "+":
                res = s[len(s) - 1] + s[len(s) - 2]
                print(res, i)
                s.append(res)
            elif i == "C":
                print(res, "C", i)
                s.pop()
            elif i == "D":
            
                res = s[len(s) - 1] * 2
                print(res, i)
                s.append(res)
            else:
                print(i)
                s.append(int(i))
        res = 0
        print(s)
        for i in s:
            res += i
        return res