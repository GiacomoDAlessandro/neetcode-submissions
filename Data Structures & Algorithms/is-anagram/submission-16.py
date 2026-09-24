class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        arrS = [0] * 26
        arrT = [0] * 26

        for i in range(len(s)):
            arrS[ord(s[i]) - ord('a')] += 1
            arrT[ord(t[i]) - ord('a')] += 1




        return arrS == arrT