class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arrS = [0] * 26
        arrT = [0] * 26
        print(len(arrT))
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            print(ord(s[i]) - ord('a'))
            arrS[ord(s[i]) - ord('a')] += 1
            arrT[ord(t[i]) - ord('a')] += 1

        return arrS == arrT

