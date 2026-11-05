# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(curr):
            if not curr:
                return float('-inf'), 0

            leftMax, leftPossibleMax = dfs(curr.left)
            rightMax, rightPossibleMax = dfs(curr.right)
            currMax = max(
            leftMax,
            rightMax,
            curr.val + leftPossibleMax + rightPossibleMax,
            rightPossibleMax + curr.val,
            leftPossibleMax + curr.val,
            curr.val)
            
            possibleMax = max(
            leftPossibleMax + curr.val,
            curr.val,
            rightPossibleMax + curr.val)

            return currMax, possibleMax
        print(dfs(root)[0])

        return dfs(root)[0]