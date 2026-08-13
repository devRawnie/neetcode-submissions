"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_map = {}
        def dfs(root):
            if not root:
                return None

            if root.val in node_map:
                return node_map[root.val]

            n = Node(root.val)
            node_map[root.val] = n
            for neigh in root.neighbors:
                n1 = dfs(neigh)
                if n1:
                    n.neighbors.append(n1)

            return n

        new_root = dfs(node)
        return new_root