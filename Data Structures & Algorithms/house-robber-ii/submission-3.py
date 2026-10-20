class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(nums):
            rob1, rob2 = 0, 0
            for num in nums:
                temp = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        steal = max(nums[0], dfs(nums[1:]), dfs(nums[:-1]))

        return steal