"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# Time: O(N) Space: O(N)
class Solution:
    def cloneGraph1(self, node, clone_map) -> 'Node':
        
        # if already present in map just return the copy of it
        if node.val in clone_map.keys():
            return clone_map[node.val]

        # create a Node and append it to map
        copy = Node(node.val)
        clone_map[node.val] = copy
        
        # DFS for each neighbour
        for neighbour in node.neighbors:
            copy.neighbors.append(self.cloneGraph1(neighbour, clone_map))

        return copy

    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        clone_map = {}

        return self.cloneGraph1(node, clone_map)
        