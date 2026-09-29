class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        o = 0
        res = []
        while o < len(word1) and o < len(word2):
            res.append(word1[o])
            res.append(word2[o])
            o += 1
        
        res.append(word1[o:])
        res.append(word2[o:])

        return "".join(res)

            
    
        