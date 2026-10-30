class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        arr = {len(s) : 1 }
        
        # (1,2,1), (12,1), (1,21)
        def dfs(curr):
            if curr in arr:
                return arr[curr]
            elif s[curr] == "0":
                return 0
            

            r = dfs(curr + 1)
            if (curr + 1 < len(s)) and (s[curr] == "1" or s[curr] == "2" and s[curr + 1] in "0123456"):
                r += dfs(curr + 2)
            arr[curr] = r
            return r
        return dfs(0)
                
        