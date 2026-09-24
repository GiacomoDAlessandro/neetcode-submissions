class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        s = []

        for i, num in enumerate(temperatures):
            while s and num > s[-1][0]:
                stackT, stackInd = s.pop()
                res[stackInd] = i - stackInd
            s.append((num,i))
        return res