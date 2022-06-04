"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        def helper(node):
            
            if not node:
                return 0
            
            max_height = 0
            
            for child in node.children:
                max_height = max(max_height,helper(child))
            
            return 1+max_height
        
        return helper(root)
        