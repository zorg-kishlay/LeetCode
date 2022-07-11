"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        # basically a level order traversal problem you just need to handle the level mapping of next
        # pointers
        if not root:
            return root
        
        queue = []
        queue.append(root)
        
        while queue:
            count = len(queue)
            level = []
            while count>0:
                count-=1
                node = queue.pop(0)
                level.append(node)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            first = level.pop(0)
            while len(level):
                nex = level.pop(0)
                first.next=nex
                first=nex
            
            first.next=None
        
        
        return root
        