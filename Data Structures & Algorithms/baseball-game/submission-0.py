class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rec = [0] * len(operations)
        j = 0
        for i, num in enumerate(operations):
            if num == "+":
                rec[j] = rec[j - 1] + rec[j - 2]
                j += 1
            elif num == "C":
                rec[j - 1] = 0
                j -= 1
            elif num == "D":
                rec[j] = rec[j - 1] * 2
                j += 1
            else:
                rec[j] = int(num)
                j += 1
                

        print(rec)
        sum = 0
        for i in rec:
            sum += i

        return sum