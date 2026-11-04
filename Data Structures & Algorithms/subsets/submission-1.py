class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = []
        path = []
        
        def dfs(curr):
            
            if curr >= len(nums):
                arr.append(path.copy())
                return
            
            path.append(nums[curr])

            dfs(curr + 1)
            path.pop()
            dfs(curr + 1)


        dfs(0)
        return arr