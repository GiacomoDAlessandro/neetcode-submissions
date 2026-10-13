# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #Find root of subroot in original tree, then
        #call dfs method checking if same tree from
        #that point
        def isSameTree(s ,t):
            if not s and not t:
                return True
            elif s and t and s.val == t.val:
                return isSameTree(s.left, t.left) and isSameTree(s.right, t.right)
            else:
                return False
                
        if not root:
            return False

        if isSameTree(root, subRoot):
            return True
            
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

        