class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        
        charSet = set()
        maxC = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxC = max(maxC, r - l + 1)
        return maxC