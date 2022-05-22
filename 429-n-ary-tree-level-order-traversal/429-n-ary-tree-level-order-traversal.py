"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
         # Space and Time : O(N)
        
        # same as level order traversal 102 just change template to add children rather than
        # left and right
        
        if not root:
            return []
        
        queue = []
        result = []
        queue.append(root)
        
        while queue:
            level = []
            no_of_nodes= len(queue) # since the queue will change we need to track this
            
            while no_of_nodes:
                node = queue.pop(0)               
                level.append(node.val)
                for child in node.children:
                    queue.append(child)               
                no_of_nodes-=1
            
            result.append(level)
        
        return result
        