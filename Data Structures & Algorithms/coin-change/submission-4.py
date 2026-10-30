class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:        
        m = {}
        def dfs(curr):
            if curr == 0:
                return 0
            if curr in m:
                return m[curr]
            
            res = float('inf')
            
            for coin in coins:
                if (curr - coin) >= 0:
                    res = min(res, 1 + dfs(curr - coin))
            m[curr] = res
            return res
        coins = dfs(amount)

        return -1 if coins >= 1e9 else coins

        