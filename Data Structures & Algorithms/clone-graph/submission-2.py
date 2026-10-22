"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #make a map to hold all nodes even w/ new copies
        m = {}

        #Through DFS here if haven't copied the node already, make a copy and return it
        def dfs(currNode):
            if currNode in m:
                #Already made a copy
                return m[currNode]
            copy = Node(currNode.val)
            m[currNode] = copy
            for i in currNode.neighbors:
                copy.neighbors.append(dfs(i))
            return copy
        return dfs(node) if node else None