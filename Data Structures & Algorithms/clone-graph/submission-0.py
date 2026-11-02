"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        original_to_copy = dict()
        def clone_node(node):
            if node in original_to_copy:
                return original_to_copy[node]
            new_node = Node(node.val)
            original_to_copy[node] = new_node
            for neighbor in node.neighbors:
                 new_node.neighbors.append(clone_node(neighbor))
            return new_node
        return clone_node(node) if node else None
        