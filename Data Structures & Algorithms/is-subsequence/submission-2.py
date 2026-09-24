class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        l = 0
        for c in t:
            if l == len(s):
                return True
            if c == s[l]:
                l += 1


        return l == len(s)