"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodes = {}
        def dfs(node):
            if node in nodes:
                return nodes[node]
            
            copy = Node(node.val)
            nodes[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            
            return copy

        if node:
            return dfs(node)
        return None