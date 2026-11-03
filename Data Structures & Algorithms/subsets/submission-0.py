class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        s = []
        path = []
        def dfs(num):
            if num == len(nums):
                s.append(path.copy())
                return
            
            path.append(nums[num])
            dfs(num+1)
            path.pop()
            dfs(num + 1)
        dfs(0)
        return s