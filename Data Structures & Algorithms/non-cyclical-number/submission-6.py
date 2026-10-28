class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(n):
            print()
            out = 0
            
            while n:
                dig = n % 10
                dig = dig ** 2
                out += dig
                n = n // 10
            return out
        s = set()
        while n not in s:
            s.add(n)
            n = sumOfSquares(n)

            if n == 1:
                return True
        
       

        return False
