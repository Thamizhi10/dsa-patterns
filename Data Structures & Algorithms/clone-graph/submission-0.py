"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtonew={}
        def dfs(node):
            if not node:
                return None
            if node in oldtonew:
                return oldtonew[node]
            n=Node(node.val)
            oldtonew[node]=n
            for neighbor in node.neighbors:
                n.neighbors.append(dfs(neighbor))
            return n
        return dfs(node)