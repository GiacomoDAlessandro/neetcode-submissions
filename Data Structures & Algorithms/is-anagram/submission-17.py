class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        tChar = [0] * 26
        sChar = [0] * 26
        for i in range(len(s)):
            tChar[ord(t[i]) - ord('a')] += 1
            sChar[ord(s[i]) - ord('a')] += 1
        return tChar == sChar