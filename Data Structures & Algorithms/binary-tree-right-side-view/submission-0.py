# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        levels = []
        def dfs(curr, level):
            #Level order traversal
            if not curr:
                return
            
            if len(levels) <= level:
                levels.append([])

            levels[level].append(curr)
            dfs(curr.left, level + 1)
            dfs(curr.right, level + 1)
        dfs(root, 0)
        arr = []
        for i in levels:
            arr.append(i[len(i) - 1].val)
        return arr