"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # looks simple but the issue starts when the random pointers points
        # to a node ahead of it like in e.x 1 node3 is pointing to node5(random pointer)
        # so doing it in 1 pass is not possible I think
        
        # O(N) space and time
        
        node_copy = {None:None} # to handle case where the current.next is None
        temp = head
        
        while temp:
            copy = Node(temp.val)
            node_copy[temp] = copy
            temp = temp.next
        
        # the above iteration creates copies of all nodes and now we can map them
        
        temp = head
        while temp:
            copy = node_copy[temp]
            copy.next = node_copy[temp.next]
            copy.random = node_copy[temp.random]
            temp = temp.next
            
            # since we have copy of our nodes it makes life easier
        
        return node_copy[head]
        