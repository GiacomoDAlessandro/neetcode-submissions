# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(newRoot: Optional[TreeNode]):
            if newRoot:
                temp = newRoot.left
                newRoot.left = newRoot.right
                newRoot.right = temp
                dfs(newRoot.left)
                dfs(newRoot.right)
            else:
                return None
        dfs(root)
        return root