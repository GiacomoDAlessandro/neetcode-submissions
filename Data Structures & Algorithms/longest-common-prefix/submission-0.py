class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:      
        for i in range(len(strs[0])):
            pref = strs[0][:i + 1]
            for s in strs:
                if not pref in s:
                    return strs[0][:i]
        return strs[0]