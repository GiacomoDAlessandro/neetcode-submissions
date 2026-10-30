class Solution:
    def countSubstrings(self, s: str) -> int:
        count = len(s)

        l,r = 0, 1

        for i in range(len(s)):
            #even
            l = i - 1
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
            l = i - 1
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        

        return count