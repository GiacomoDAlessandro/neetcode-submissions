class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def dfs(low, high):
            if low > high: 
                return None
            m = (low + high) // 2
            return TreeNode(nums[m], dfs(low, m - 1), dfs(m + 1, high))

        return dfs(0, len(nums) - 1)        