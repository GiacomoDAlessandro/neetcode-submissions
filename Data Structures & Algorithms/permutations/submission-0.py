class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(cur, rest):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for i, added in enumerate(rest):
                if added == False:
                    rest[i] = True
                    cur.append(nums[i])
                    dfs(cur, rest)
                    cur.pop()
                    rest[i] = False
            


        r = [False] * len(nums)

        dfs([], r)

        return res