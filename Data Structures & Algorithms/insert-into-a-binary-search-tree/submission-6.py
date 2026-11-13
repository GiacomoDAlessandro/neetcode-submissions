# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def dfs(curr, prev):
            if not curr:
                if not prev:
                    return TreeNode(val)
                if prev.val > val:
                    prev.left = TreeNode(val)
                else:
                    prev.right = TreeNode(val)
                return
            if curr.val > val:
                dfs(curr.left, curr)
            else:
                dfs(curr.right, curr)

            

        return dfs(root, None) if dfs(root, None) else root

