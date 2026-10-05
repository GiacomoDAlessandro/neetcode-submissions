class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxC = 0
        d = {}
        l = 0
        maxF = 0
        for r, char in enumerate(s):
            d[s[r]] = 1 + d.get(s[r], 0)
            maxF = max(maxF, d[s[r]])
            
            while (r -l + 1) - maxF > k:
                d[s[l]] -= 1
                l += 1

            maxC = max(maxC, r - l + 1)

            
        return maxC
        
            