"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #Recursion since you don't know when it'll end

        m = {}

        def dfs(curr):
            if curr in m:
                return m[curr]
            
            copy = Node(curr.val)
            m[curr] = copy
            
            for new in curr.neighbors:
                copy.neighbors.append(dfs(new))
            return copy
            
        return dfs(node) if node else None
        