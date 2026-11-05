class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n <= 1:
            return 0
        else:
            if n % 2 == 0:
                return self.numberOfMatches(n // 2) + n // 2
            else:
                return self.numberOfMatches(n - 1) + 1
        
