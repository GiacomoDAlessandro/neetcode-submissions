class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        for i in range(len(s)):
            l, r = 0, len(s) - 1
            while l <= r:
                if l == i:
                    l += 1
                elif r == i:
                    r -= 1
                if s[l] != s[r]:
                    break
                l += 1
                r -= 1
            if l > r:
                return True
        return False

        
