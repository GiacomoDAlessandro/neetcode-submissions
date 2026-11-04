class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortestLen = len(strs[0])
        for i in strs:
            shortestLen = min(shortestLen, len(i))
        pref = ""
        for i in range(shortestLen):
            q = strs[0][i]
            for j in strs:
                if q != j[i]:
                    print(q,i,shortestLen)
                    return pref
            pref = pref + q
        return pref