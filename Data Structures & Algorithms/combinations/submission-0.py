class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = set()

        def dfs(i, cur):
            if len(cur) == k:
                res.add(tuple(cur))
                return
            if i > n:
                return
            cur.append(i)
            dfs(i + 1, cur)
            cur.pop()
            dfs(i + 1, cur)

        dfs(1, [])

        return [list(t) for t in res]