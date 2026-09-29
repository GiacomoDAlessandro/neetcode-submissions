class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = min(len(word1), len(word2))
        
        res = ""
        a = 0
        for i in range(l):
            res += word1[i] + word2[i]
            if i == len(word1) - 1 and len(word1) != len(word2):
                res += word2[i + 1:len(word2)]
            elif i == len(word2) - 1 and len(word1) != len(word2):
                res += word1[i + 1:len(word1)]
        
        return res
        