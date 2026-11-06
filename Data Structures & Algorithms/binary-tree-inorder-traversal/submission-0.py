# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        def dfs(curr):

            if not curr:
                return
            else:
                dfs(curr.left)
                l.append(curr.val)
                dfs(curr.right)
        dfs(root)
        return l