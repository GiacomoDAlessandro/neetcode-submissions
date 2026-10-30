class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        

        l,r = 0, 0
        m = s[0]
        for i in range(len(s)):
            #even
            l = i - 1
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(s[l: r + 1]) > len(m):
                    m = s[l: r + 1]
                l -= 1
                r += 1
                    
            
            #odd
            l = i - 1
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(s[l: r + 1]) > len(m):
                    m = s[l: r + 1]
                l -= 1
                r += 1
                

        return m