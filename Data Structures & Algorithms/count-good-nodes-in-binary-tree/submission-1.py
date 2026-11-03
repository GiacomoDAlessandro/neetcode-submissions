# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        curVal = 0

        def dfs(curr, num):
            if not curr:
                return
            nonlocal curVal 
            if curr.val >= num:
                print(curr.val)
                curVal += 1

            dfs(curr.right, max(num, curr.val))
            dfs(curr.left, max(num, curr.val))

        dfs(root, float('-inf'))
        return curVal
