class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def dfs(cur, rest):
            if len(cur) == len(nums):
                res.add(tuple(cur))
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

        return list(res)