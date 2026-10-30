class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        

        l,r = 0, 1
        m = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                newS = s[i:j + 1]
                if len(newS) > len(m) and newS == newS[::-1]:
                    m = newS
                    


        return m