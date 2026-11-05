# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxSum = float('-inf')
        def dfs(curr):
            if not curr:
                return 0

            leftPossibleMax = dfs(curr.left)
            rightPossibleMax = dfs(curr.right)
            nonlocal maxSum

            maxSum = max(
            maxSum,
            maxSum,
            curr.val + leftPossibleMax + rightPossibleMax,
            rightPossibleMax + curr.val,
            leftPossibleMax + curr.val,
            curr.val)
            
            possibleMax = max(
            leftPossibleMax + curr.val,
            curr.val,
            rightPossibleMax + curr.val)

            return possibleMax
        dfs(root)
        return maxSum