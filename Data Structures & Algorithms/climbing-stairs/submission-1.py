class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        prev1 = 1
        prev2 = 2

        for i in range(2, n):
            temp = prev1
            prev1 = prev2
            prev2 = temp + prev2
        return prev2